# Generated by Django 5.1.5 on 2025-01-23 18:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('task_manager', '0001_initial'),
        ('team', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='owner',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name='task',
            name='team_id',
            field=models.ForeignKey(
                blank=True,
                db_column='team_id',
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='team.team',
            ),
        ),
        migrations.AddField(
            model_name='taskhistory',
            name='task_id',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='task_manager.task'
            ),
        ),
        migrations.AddField(
            model_name='task',
            name='cycle',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='okr.cycle',
            ),
        ),
    ]
