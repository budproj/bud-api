import uuid6

from django.db import models

from user.enums.user_choices import UserStatusChoices
from user.enums.user_settings_choices import UserSettingsKeyChoices

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
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
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid6.uuid7, null=False, blank=False) # initial
    authz_sub = models.CharField() # initial
    role = models.CharField(blank=True, null=True) # initial
    picture = models.CharField(blank=True, null=True) # initial
    gender = models.TextField(blank=True, null=True) # initial
    first_name = models.CharField() # initial
    last_name = models.CharField(blank=True, null=True) # initial
    nickname = models.CharField(blank=True, null=True) # initial
    linked_in_profile_address = models.CharField(blank=True, null=True) # initial
    about = models.TextField(blank=True, null=True) # initial
    email = models.TextField(db_collation="und-x-icu", unique=True) # initial
    status = models.TextField(choices=UserStatusChoices)  # initial
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True) # initial
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True) # initial
    deleted_at = models.DateTimeField(null=True, blank=True)

    # Gerenciador customizado
    objects = CustomUserManager()

    # Campos excluidos do BaseUser
    groups = None
    user_permissions = None
    password = None
    last_login = None
    is_active = None
    is_superuser = None
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.id + ' | ' + self.first_name + ' ' + self.last_name if self.last_name != None else ""
    
    class Meta:
        db_table = 'user'

class UserSetting(BaseModel):
    key = models.TextField(choices=UserSettingsKeyChoices) # initial
    value = models.CharField() # initial
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user_id') # initial
    preferences = models.JSONField() # initial

    class Meta:
        db_table = 'user_setting'
