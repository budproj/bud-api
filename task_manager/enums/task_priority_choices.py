from django.db import models


class TaskPriorityChoices(models.IntegerChoices):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    VERY_HIGH = 4
