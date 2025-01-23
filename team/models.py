from django.db import models

from api.base.base_model import BaseModel
from user.models import User

class Team(BaseModel):
    name = models.CharField()
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', models.CASCADE, blank=True, null=True)
    owner = models.ForeignKey(User, models.CASCADE,null=False, blank=False)
    users = models.ManyToManyField(User, through='TeamUsersUser', related_name='Team_users')
    
    class Meta:
        db_table = 'team'


class TeamUsersUser(models.Model):
    team_id = models.ForeignKey(Team, models.CASCADE) 
    user_id = models.ForeignKey(User, models.CASCADE)

    class Meta:
        db_table = 'team_users_user'