# Generated by Django 5.1.5 on 2025-02-19 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0004_task_cycle_task_orderindex_alter_taskhistory_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='initial_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
