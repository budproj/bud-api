from django.db import models

from api.base.base_model import BaseModel
from user.models import User

class Team(BaseModel):
    name = models.CharField()
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', models.CASCADE, blank=True, null=True)
    owner = models.ForeignKey(User, models.CASCADE,null=False, blank=False)

    class Meta:
        db_table = 'team'


class TeamUsersUser(models.Model):
    team_id = models.OneToOneField(Team, models.CASCADE) 
    user_id = models.ForeignKey(User, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'team_users_user'
        unique_together = (('team_id', 'user_id'),)