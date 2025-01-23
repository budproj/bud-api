from django.db import models
from django.contrib.postgres.fields import ArrayField

from api.base.base_model import BaseModel
from team.models import Team
from user.models import User
from okr.models import KeyResult

from .enums import TaskStatusChoices, TaskPriorityChoices
        
class Task(BaseModel):
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True, db_column='team_id')
    key_result_id = models.ForeignKey(KeyResult, on_delete=models.CASCADE, blank=True, null=True, db_column='key_result_id')
    status = models.TextField(
        choices=TaskStatusChoices,
        default=TaskStatusChoices.PENDING,
        null=False, blank=False
    )
    title = models.TextField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    priority = models.IntegerField(choices=TaskPriorityChoices, null=False, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    support_team = ArrayField(models.TextField(), blank=True, null=True)
    attachments = ArrayField(models.TextField(), blank=True, null=True)
    tags = ArrayField(models.TextField(), blank=True, null=True)

    def save(self, *args, **kwargs):
        # identify if user is being created ou updated
        try:
            old_instance = Task.objects.get(id=self.id)
            # pass thru fields searching for changes
            for field in self._meta.fields:
                field_name = field.name
                old_value = getattr(old_instance, field_name)
                new_value = getattr(self, field_name)
                # stores the changed field
                if old_value != new_value:
                    history = TaskHistory()
                    history.task_id = self
                    history.field = field_name
                    history.old_state = old_value
                    history.new_state = new_value
                    user = kwargs.pop('user', None) 
                    history.author = user
                    history.save()
        except Task.DoesNotExist:
            pass
            
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = 'task'


class TaskHistory(BaseModel):
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    field = models.TextField(null=False, blank=False)
    old_state = models.TextField()
    new_state = models.TextField()
    author = models.TextField()
    
    def __str__(self):
        return str(self.uuid)

    class Meta:
        db_table = 'task_history'
