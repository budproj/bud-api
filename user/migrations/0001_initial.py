# Generated by Django 5.1.5 on 2025-01-23 18:06

import django.db.models.deletion
import uuid6
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid6.uuid7, primary_key=True, serialize=False)),
                ('authz_sub', models.CharField()),
                ('role', models.CharField(blank=True, null=True)),
                ('picture', models.CharField(blank=True, null=True)),
                ('gender', models.TextField(blank=True, null=True)),
                ('first_name', models.CharField()),
                ('last_name', models.CharField(blank=True, null=True)),
                ('nickname', models.CharField(blank=True, null=True)),
                ('linked_in_profile_address', models.CharField(blank=True, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('email', models.TextField(db_collation='und-x-icu', unique=True)),
                ('status', models.TextField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')])),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='UserSetting',
            fields=[
                ('id', models.UUIDField(default=uuid6.uuid7, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('key', models.TextField(choices=[('LOCALE', 'Locale')])),
                ('value', models.CharField()),
                ('preferences', models.JSONField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_setting',
            },
        ),
    ]
