from django.db import models

class KeyResultCheckMarkStateChoices(models.TextChoices):
    CHECKED = 'CHECKED'
    UNCHECKED = 'UNCHECKED'