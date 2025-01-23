from django.db import models
from django.contrib.postgres.fields import ArrayField

from api.base.base_model import BaseModel
from team.models import Team
from okr.models import Cycle, KeyResult

from .enums import TaskStatusChoices, TaskPriorityChoices
        
class Task(BaseModel):
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    kr_id = models.ForeignKey(KeyResult, null=True, blank=True, on_delete=models.CASCADE)
    cycle_id = models.ForeignKey(Cycle, null=True, blank=True, on_delete=models.CASCADE)
    user_id = models.TextField(null=False, blank=False)
    status = models.TextField(
        choices=TaskStatusChoices,
        default=TaskStatusChoices.PENDING,
        null=False, blank=False
    )
    title = models.TextField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    priority = models.IntegerField(choices=TaskPriorityChoices, null=False, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    initial_date = models.DateTimeField(null=False)
    owner = models.TextField(null=False, blank=False)
    support_team = ArrayField(models.TextField())
    attachments = ArrayField(models.TextField(), blank=True)
    tags = ArrayField(models.TextField(), blank=True)
    orderindex = models.IntegerField(null=False, blank=False)

    def save(self, *args, **kwargs):
        if self.pk: 
            try:
                old_instance = Task.objects.get(pk=self.pk)
            except Task.DoesNotExist:
                old_instance = None  

            if old_instance:
                
                for field in self._meta.fields:
                    field_name = field.name
                    old_value = getattr(old_instance, field_name)
                    new_value = getattr(self, field_name)

                    if old_value != new_value:
                        history = TaskHistory()
                        history.task_id = self
                        history.field = field_name
                        history.old_state = old_value
                        history.new_state = new_value
                        user = kwargs.pop('user', None) 
                        history.author = user
                        history.save()
                    
        super().save(*args, **kwargs)

        
    def __str__(self):
        return str(self.uuid)
    
    class Meta:
        db_table = 'task'


class TaskHistory(BaseModel):
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='history')
    field = models.TextField(null=False, blank=False)
    old_state = models.TextField()
    new_state = models.TextField()
    author = models.TextField()
    
    def __str__(self):
        return str(self.uuid)

    class Meta:
        db_table = 'task_history'
