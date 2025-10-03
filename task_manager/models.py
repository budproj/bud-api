from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.timezone import now

from api.models import BaseModel
from team.models import TeamORM
from user.models import UserORM

from django.db import connection

class TaskManager(models.Manager):
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

class TaskORM(BaseModel):
    class TaskStatusChoices(models.TextChoices):
        PENDING = 'pending'
        TO_DO = 'toDo'
        DOING = 'doing'
        DONE = 'done'
        
    class TaskPriorityChoices(models.IntegerChoices):
        LOW = 1
        MEDIUM = 2
        HIGH = 3
        VERY_HIGH = 4
        
    team = models.ForeignKey(
        TeamORM, on_delete=models.CASCADE, blank=True, null=True, db_column='team_id'
    )
    key_result = models.ForeignKey(
        'key_result.KeyResultORM',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        db_column='key_result_id',
        related_name='task_key_result',
    )
    cycle = models.ForeignKey(
        'cycle.CycleORM', null=True, blank=True, on_delete=models.CASCADE, db_column='cycle_id'
    )
    owner = models.ForeignKey(UserORM, null=False, blank=False, on_delete=models.CASCADE)
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
            old_version = TaskORM.objects.get(pk=self.pk)
        except TaskORM.DoesNotExist:
            is_new = True
            
        super().save(*args, **kwargs)
        if not is_new and old_version and user_id:
            excluded_from_history = ['updated_at', 'support_team']
            user = UserORM.objects.get(id=user_id)
            for field in self._meta.fields:
                field_name = field.name
                if field_name not in excluded_from_history:
                    old_value = getattr(old_version, field_name, None)
                    new_value = getattr(self, field_name, None)

                    if old_value != new_value:
                        self._register_history(self, field_name, old_value, new_value, user)
                    
        if self.key_result:
            users = [str(self.owner.id)] + self.support_team # type: ignore - support_team: List(str)
            result = UserORM.objects.check_users_role(str(self.key_result.id), users) # type: ignore - function in user.models.CustomUserManager.check_users_role
            for i in result:
                if i.user_role not in ['owner', 'support_team_member']:
                    TaskORM.objects.insert_user_in_kr_team_support(str(self.key_result.id), str(i.id)) # type: ignore - function in task_manager.models.TaskManager.insert_user_in_kr_team_support
                
    
    def _register_history(self, task, name, old, new, user):
        TaskHistoryORM.objects.create(
            task=task,
            field=name,
            old_state=old,
            new_state=new,
            author=user if user else None,
        )

    def delete_task(self, user=None):
        if not self.deleted_at:
            self.deleted_at = now()
            self.save()

    class Meta:
        db_table = 'task'
        managed = False


class TaskHistoryORM(BaseModel):
    task = models.ForeignKey(TaskORM, on_delete=models.CASCADE, related_name='history')
    field = models.TextField(null=False, blank=False)
    old_state = models.TextField(null=True, blank=True)
    new_state = models.TextField(null=True, blank=True)
    author = models.ForeignKey(UserORM, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return f'History of Task {self.task} - {self.field}'

    class Meta:
        db_table = 'task_history'
        verbose_name_plural = 'Task Histories'
        managed = False


class TaskCommentsORM(BaseModel):
    text = models.TextField(blank=True, null=True)
    task = models.ForeignKey(TaskORM, models.CASCADE)
    user = models.ForeignKey(UserORM, models.CASCADE)
    parent = models.ForeignKey('self', models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'task_comment'
        verbose_name_plural = 'Task Comments'
        managed = False

    def soft_delete(self):
        self.deleted_at = now()
        self.save()