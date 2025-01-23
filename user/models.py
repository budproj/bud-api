import uuid6

from django.db import models

from user.enums.user_choices import UserStatusChoices
from user.enums.user_settings_choices import UserSettingsKeyChoices

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from api.base.base_model import BaseModel

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('role', 'GOD')
        # extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid6.uuid7, null=False, blank=False)
    authz_sub = models.CharField()
    role = models.CharField(blank=True, null=True)
    picture = models.CharField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True) 
    first_name = models.CharField()
    last_name = models.CharField(blank=True, null=True)
    nickname = models.CharField(blank=True, null=True)
    linked_in_profile_address = models.CharField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    email = models.TextField(db_collation="und-x-icu", unique=True)
    status = models.TextField(choices=UserStatusChoices)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()
    groups = None

    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    class Meta:
        db_table = 'user'


class UserSetting(BaseModel):
    key = models.TextField(choices=UserSettingsKeyChoices)
    value = models.CharField()
    user = models.ForeignKey(User, models.DO_NOTHING)
    preferences = models.JSONField()

    class Meta:
        db_table = 'user_setting'