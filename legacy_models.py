from django.db import models


class Migrations(models.Model):
    timestamp = models.BigIntegerField()
    name = models.CharField()

    class Meta:
        managed = False
        db_table = 'migrations'


class Task(models.Model):
    id = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('User', models.DO_NOTHING)
    assigned_user = models.ForeignKey(
        'User',
        models.DO_NOTHING,
        related_name='task_assigned_user_set',
        blank=True,
        null=True,
    )
    description = models.TextField()
    state = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'task'


class TypeormMetadata(models.Model):
    type = models.CharField()
    database = models.CharField(blank=True, null=True)
    schema = models.CharField(blank=True, null=True)
    table = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typeorm_metadata'
