from django.db import models


class TaskStatusChoices(models.TextChoices):
    PENDING = 'pending'
    TO_DO = 'toDo'
    DOING = 'doing'
    DONE = 'done'
