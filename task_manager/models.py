from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.timezone import now

from api.base.base_model import BaseModel
from team.models import Team
from okr.models import Cycle, KeyResult
from user.models import User

from django.db import connection

from .enums import TaskStatusChoices, TaskPriorityChoices

class TaskManager(models.Manager):
    def check_if_task_owner_in_kr_team(self, task: str):
        query = """
            SELECT
                tk.id,
                CASE
                    WHEN EXISTS (SELECT 1 FROM key_result WHERE id = tk.key_result_id AND owner_id = tk.owner_id) THEN 'owner'
                    WHEN EXISTS (SELECT 1 FROM key_result_support_team_members_user WHERE key_result_id = tk.key_result_id AND user_id = tk.owner_id) THEN 'support_team_member'
                    ELSE NULL 
                END AS user_role
            FROM
                task tk
            WHERE
                tk.id = %s
        """
        
        result = Task.objects.raw(query, [task])
        
        if result: 
            return result
        return None

    def insert_user_in_kr_team_support(self, kr, user):
        query = """
            INSERT INTO
                key_result_support_team_members_user
                    (key_result_id, user_id)
            VALUES
                (%s, %s)
        """
        with connection.cursor() as cursor:
            cursor.execute(query, [kr, user])

class Task(BaseModel):
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, blank=True, null=True, db_column='team_id'
    )
    key_result = models.ForeignKey(
        KeyResult,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        db_column='key_result_id',
        related_name='task_key_result',
    )
    cycle = models.ForeignKey(
        Cycle, null=True, blank=True, on_delete=models.CASCADE, db_column='cycle_id'
    )
    owner = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    status = models.TextField(
        choices=TaskStatusChoices.choices,
        default=TaskStatusChoices.PENDING,
        null=False,
        blank=False,
    )
    title = models.TextField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    priority = models.IntegerField(
        choices=TaskPriorityChoices.choices, null=False, blank=True
    )
    initial_date = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    support_team = ArrayField(models.TextField(), blank=True, null=True)
    attachments = ArrayField(models.TextField(), blank=True, null=True)
    tags = ArrayField(models.TextField(), blank=True, null=True)
    orderindex = models.IntegerField(null=True, blank=True)
    objects = TaskManager()
    
    def save(self, *args, **kwargs): 
        is_new = False
        old_version = None
        user_id = kwargs.pop('usuario_logado', None)
        
        try:
            old_version = Task.objects.get(pk=self.pk)
        except Task.DoesNotExist:
            is_new = True
            
        super().save(*args, **kwargs)
        if not is_new and old_version:
            excluded_from_history = ['updated_at', 'support_team']
            user = User.objects.get(id=user_id)
            for field in self._meta.fields:
                field_name = field.name
                if field_name not in excluded_from_history:
                    old_value = getattr(old_version, field_name, None)
                    new_value = getattr(self, field_name, None)

                    if old_value != new_value:
                        self._register_history(self, field_name, old_value, new_value, user)
                    
        if self.key_result:
            result = Task.objects.check_if_task_owner_in_kr_team(str(self.id))
            if result and result[0].user_role not in ['owner', 'support_team_member']:
                Task.objects.insert_user_in_kr_team_support(str(self.key_result.id), str(self.owner.id))
    
    def _register_history(self, task, name, old, new, user):
        TaskHistory.objects.create(
            task=task,
            field=name,
            old_state=old,
            new_state=new,
            author=user if user else None,
        )

    def delete_task(self, user=None):
        if not self.deleted_at:
            self.deleted_at = now()
            self.save(update_fields=['deleted_at'])

    class Meta:
        db_table = 'task'


class TaskHistory(BaseModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='history')
    field = models.TextField(null=False, blank=False)
    old_state = models.TextField(null=True, blank=True)
    new_state = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return f'History of Task {self.task} - {self.field}'

    class Meta:
        db_table = 'task_history'
        verbose_name_plural = 'Task Histories'


class TaskComments(BaseModel):
    text = models.TextField(blank=True, null=True)
    task = models.ForeignKey(Task, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    parent = models.ForeignKey('self', models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'task_comment'
        verbose_name_plural = 'Task Comments'

    def soft_delete(self):
        self.deleted_at = now()
        self.save()