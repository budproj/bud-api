import uuid6

from django.db import models

from api.base.base_model import BaseModel
from user.models import User

class Team(BaseModel):
    class GENDER(models.TextChoices):
        MALE = "Male"
        FEMALE = "Female"
        NEUTRAL = "Neutral"
        
    name = models.CharField() # initial
    description = models.TextField(blank=True, null=True) # initial
    parent = models.ForeignKey('self', models.CASCADE, blank=True, null=True, db_column='parent_id') # initial
    owner = models.ForeignKey(User, models.CASCADE,null=False, blank=False, db_column='owner_id') # initial
    users = models.ManyToManyField(User, through='TeamUsersUser', related_name='Team_users') # initial
    gender = models.TextField(choices=GENDER) # initial
    
    class Meta:
        db_table = 'team'


class TeamUsersUser(models.Model):
    team = models.ForeignKey(Team, models.CASCADE) # initial
    user = models.ForeignKey(User, models.CASCADE) # initial

    class Meta:
        db_table = 'team_users_user'