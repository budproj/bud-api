from django.db import models
from api.base.base_model import BaseModel

class Team(BaseModel):
    name = models.CharField()
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey('User', null=False, blank=False)

    class Meta:
        db_table = 'team'


class TeamUsersUser(models.Model):
    team_id = models.OneToOneField(Team, models.DO_NOTHING) 
    user_id = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'team_users_user'
        unique_together = (('team', 'user'),)