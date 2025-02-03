from django.db import models


class KeyResultTypeChoices(models.TextChoices):
    ASCENDING = 'ASCENDING'
    DESCENDING = 'DESCENDING'


class KeyResultFormatChoices(models.TextChoices):
    NUMBER = 'NUMBER'
    PERCENTAGE = 'PERCENTAGE'
    COIN_BRL = 'COIN_BRL'
    COIN_USD = 'COIN_USD'
    COIN_EUR = 'COIN_EUR'
    COIN_GBP = 'COIN_GBP'


class KeyResultModeChoices(models.TextChoices):
    COMPLETED = 'COMPLETED'
    PUBLISHED = 'PUBLISHED'
    DRAFT = 'DRAFT'
    DELETED = 'DELETED'

