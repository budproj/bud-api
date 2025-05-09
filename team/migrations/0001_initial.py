# Generated by Django 5.1.5 on 2025-02-03 21:02

import django.db.models.deletion
import uuid6
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.UUIDField(default=uuid6.uuid7, primary_key=True, serialize=False)),
                ('name', models.CharField()),
                ('description', models.TextField(blank=True, null=True)),
                ('gender', models.TextField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Neutral', 'Neutral')])),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('owner', models.ForeignKey(db_column='owner_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, db_column='parent_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='team.team')),
            ],
            options={
                'db_table': 'team',
            },
        ),
        migrations.CreateModel(
            name='TeamUsersUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'team_users_user',
            },
        ),
        migrations.AddField(
            model_name='team',
            name='users',
            field=models.ManyToManyField(related_name='Team_users', through='team.TeamUsersUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
