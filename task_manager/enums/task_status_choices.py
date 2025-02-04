from django.db import models


class TaskStatusChoices(models.TextChoices):
    PENDING = 'Pending'
    TO_DO = 'To Do'
    DOING = 'Doing'
    DONE = 'Done'
