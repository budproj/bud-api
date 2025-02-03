from django.db import models


class CycleCadenceChoices(models.TextChoices):
    YEARLY = 'YEARLY'
    QUARTERLY = 'QUARTERLY'

