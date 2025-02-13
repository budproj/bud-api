# Generated by Django 5.1.5 on 2025-02-03 21:02

import django.contrib.postgres.fields
import django.db.models.deletion
import uuid6
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('okr', '0001_initial'),
        ('team', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid6.uuid7, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.TextField(choices=[('Pending', 'Pending'), ('To Do', 'To Do'), ('Doing', 'Doing'), ('Done', 'Done')], default='Pending')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('priority', models.IntegerField(blank=True, choices=[(1, 'Low'), (2, 'Medium'), (3, 'High'), (4, 'Very High')])),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('support_team', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, null=True, size=None)),
                ('attachments', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, null=True, size=None)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, null=True, size=None)),
                ('key_result', models.ForeignKey(blank=True, db_column='key_result_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='okr.keyresult')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(blank=True, db_column='team_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='team.team')),
            ],
            options={
                'db_table': 'task',
            },
        ),
        migrations.CreateModel(
            name='TaskHistory',
            fields=[
                ('id', models.UUIDField(default=uuid6.uuid7, primary_key=True, serialize=False)),
                ('field', models.TextField()),
                ('old_state', models.TextField()),
                ('new_state', models.TextField()),
                ('author', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_manager.task')),
            ],
            options={
                'db_table': 'task_history',
            },
        ),
    ]
