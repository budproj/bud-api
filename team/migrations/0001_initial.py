# Generated by Django 5.1.5 on 2025-01-23 18:06

import uuid6
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.UUIDField(default=uuid6.uuid7, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'team',
            },
        ),
        migrations.CreateModel(
            name='TeamUsersUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'team_users_user',
            },
        ),
    ]