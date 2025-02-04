from django.db import models


class ObjectiveModeChoices(models.TextChoices):
    COMPLETED = 'COMPLETED'
    PUBLISHED = 'PUBLISHED'
    DRAFT = 'DRAFT'
    DELETED = 'DELETED'

