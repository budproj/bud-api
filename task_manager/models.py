from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.timezone import now

from api.base.base_model import BaseModel
from team.models import Team
from okr.models import Cycle, KeyResult
from user.models import User

from .enums import TaskStatusChoices, TaskPriorityChoices


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
    description = models.TextField(null=False, blank=False)
    priority = models.IntegerField(
        choices=TaskPriorityChoices.choices, null=False, blank=True
    )
    due_date = models.DateTimeField(null=True, blank=True)
    support_team = ArrayField(models.TextField(), blank=True, null=True)
    attachments = ArrayField(models.TextField(), blank=True, null=True)
    tags = ArrayField(models.TextField(), blank=True, null=True)
    orderindex = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        user = kwargs.pop('user', None)

        is_new = not bool(self.pk)

        old_instance = None
        if not is_new:
            try:
                old_instance = Task.objects.get(pk=self.pk)
            except Task.DoesNotExist:
                pass

        super().save(*args, **kwargs)

        if is_new:
            TaskHistory.objects.create(
                task=self,
                field='created',
                old_state='NULL',
                new_state='Task criada',
                author=user.username if user else 'System',
            )
        elif old_instance:
            self._register_history(old_instance, user)

    def delete_task(self, user=None):
        if not self.deleted_at:
            old_deleted_at = self.deleted_at

            self.deleted_at = now()

            self.save(update_fields=['deleted_at'])

            self._register_history('deleted_at', old_deleted_at, self.deleted_at, user)

    def _register_history(self, field, old_state, new_state, user):
        for field in self._meta.fields:
            field_name = field.name
            old_value = getattr(old_state, field_name, None)
            new_value = getattr(self, field_name, None)

            if old_value != new_value:
                TaskHistory.objects.create(
                    task=self,
                    field=field_name,
                    old_state=str(old_value) if old_value is not None else 'NULL',
                    new_state=str(new_value) if new_value is not None else 'NULL',
                    author=user.username if user else 'System',
                )

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'task'


class TaskHistory(BaseModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='history')
    field = models.TextField(null=False, blank=False)
    old_state = models.TextField(null=True, blank=True)
    new_state = models.TextField(null=True, blank=True)
    author = models.TextField(null=False, blank=False)

    def __str__(self):
        return f'History of Task {self.task} - {self.field}'

    class Meta:
        db_table = 'task_history'
        verbose_name_plural = 'Task Histories'
