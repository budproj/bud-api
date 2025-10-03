from django.db import models

from api.models import BaseModel
from key_result.models import KeyResultORM


class ObjectiveORM(BaseModel):
    class ObjectiveModeChoices(models.TextChoices):
        COMPLETED = 'COMPLETED'
        PUBLISHED = 'PUBLISHED'
        DRAFT = 'DRAFT'
        DELETED = 'DELETED'
    
    title = models.CharField()
    cycle = models.ForeignKey('cycle.CycleORM', models.CASCADE)
    owner = models.ForeignKey('user.UserORM', models.CASCADE)
    team = models.ForeignKey('team.TeamORM', models.CASCADE, blank=True, null=True)
    description = models.CharField(blank=True, null=True)
    mode = models.TextField(choices=ObjectiveModeChoices.choices)
    
    def save(self, *args, **kwargs):
        old_version = ObjectiveORM.objects.get(pk=self.pk)
        if self.team and old_version.team and old_version.team.id != self.team.id:
            self.update_team(self.team.id)
        super().save(*args, **kwargs)
        
    def update_team(self, team_id):
        KeyResultORM.objects.filter(objective_id=self.id).update(team_id=team_id)
        
    class Meta:
        db_table = 'objective'
        managed = False