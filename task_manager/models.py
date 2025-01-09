from django.db import models
from django.contrib.postgres.fields import ArrayField

from api.base.base_model import BaseModel
from .enums import TaskStatusChoices, TaskPriorityChoices

#TODO: move this model for team application later 
class Team(BaseModel):
    name = models.CharField()
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    owner = models.UUIDField(null=False, blank=False)

    class Meta:
        db_table = 'team'
        
class Task(BaseModel):
    team_id = models.ForeignKey('Team', on_delete=models.CASCADE)
    status = models.TextField(
        choices=TaskStatusChoices,
        default=TaskStatusChoices.PENDING,
        null=False, blank=False
    )
    title = models.TextField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    priority = models.IntegerField(choices=TaskPriorityChoices, null=False, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    initial_date = models.DateTimeField(null=True, blank=True)
    owner = models.TextField(null=False, blank=False)
    support_team = ArrayField(models.TextField())
    #order_index = models.AutoField(unique=True)
    attachments = ArrayField(models.TextField())
    tags = ArrayField(models.TextField())

    def __str__(self):
        return str(self.uuid)
    
    class Meta:
        db_table = 'task'

class TaskHistory(BaseModel):
    task_id = models.ForeignKey('Task', on_delete=models.CASCADE)
    field = models.TextField(null=False, blank=False)
    old_state = models.TextField()
    new_state = models.TextField()
    author = models.TextField()
    
    def __str__(self):
        return str(self.uuid)

    class Meta:
        db_table = 'task_'
