from django.db import models
from api.models import BaseModel


class CycleORM(BaseModel):
    class CycleCadenceChoices(models.TextChoices):
        YEARLY = 'YEARLY'
        QUARTERLY = 'QUARTERLY'
    
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    team = models.ForeignKey('team.TeamORM', models.CASCADE)
    period = models.CharField()
    cadence = models.TextField(choices=CycleCadenceChoices.choices)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField()

    class Meta:
        db_table = 'cycle'
        managed = False
