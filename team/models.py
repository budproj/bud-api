from django.db import models

from api.models import BaseModel
from user.models import UserORM


class TeamORM(BaseModel):
    class GENDER(models.TextChoices):
        MALE = "Male"
        FEMALE = "Female"
        NEUTRAL = "Neutral"
        
    name = models.CharField() # initial
    description = models.TextField(blank=True, null=True) # initial
    parent = models.ForeignKey('self', models.CASCADE, blank=True, null=True, db_column='parent_id') # initial
    owner = models.ForeignKey(UserORM, models.CASCADE,null=False, blank=False, db_column='owner_id') # initial
    users = models.ManyToManyField(UserORM, through='TeamUsersUserORM', related_name='Team_users') # initial
    gender = models.TextField(choices=GENDER.choices) # initial
    
    class Meta:
        db_table = 'team'
        managed = False

class TeamUsersUserORM(models.Model):
    team = models.ForeignKey(TeamORM, models.CASCADE) # initial
    user = models.ForeignKey(UserORM, models.CASCADE) # initial

    class Meta:
        db_table = 'team_users_user'
        managed = False

class TeamCompany(models.Model):
    """
    Materialized view that unify Teams and Companies
    """
    id = models.IntegerField(primary_key=True)
    company = models.ForeignKey('TeamORM', on_delete=models.CASCADE, related_name='team_company_company_id')
    team = models.ForeignKey('TeamORM', on_delete=models.CASCADE, related_name='team_company_team_id')
    depth = models.IntegerField()
    
    class Meta:
        db_table = 'team_company'
        managed = False