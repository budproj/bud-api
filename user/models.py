from django.db import models
from django.contrib.postgres.fields import CITextField

from user.enums.user_choices import UserStatusChoices
from user.enums.user_settings_choices import UserSettingsKeyChoices

from api.base.base_model import BaseModel

class User(BaseModel):
    authz_sub = models.CharField()
    role = models.CharField(blank=True, null=True)
    picture = models.CharField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True) 
    first_name = models.CharField()
    last_name = models.CharField(blank=True, null=True)
    nickname = models.CharField(blank=True, null=True)
    linked_in_profile_address = models.CharField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    email = CITextField(unique=True)
    status = models.TextField(choices=UserStatusChoices)

    class Meta:
        db_table = 'user'


class UserSetting(BaseModel):
    key = models.TextField(choices=UserSettingsKeyChoices)
    value = models.CharField()
    user = models.ForeignKey(User, models.DO_NOTHING)
    preferences = models.JSONField()

    class Meta:
        db_table = 'user_setting'