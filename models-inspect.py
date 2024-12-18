# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cycle(models.Model):
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.UUIDField(primary_key=True)
    team = models.ForeignKey('Team', models.DO_NOTHING)
    period = models.CharField()
    cadence = models.TextField()  # This field type is a guess.
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cycle'


class KeyResult(models.Model):
    title = models.CharField()
    goal = models.DecimalField(max_digits=65535, decimal_places=65535)
    initial_value = models.DecimalField(max_digits=65535, decimal_places=65535)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    format = models.TextField()  # This field type is a guess.
    id = models.UUIDField(primary_key=True)
    objective = models.ForeignKey('Objective', models.DO_NOTHING)
    team = models.ForeignKey('Team', models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey('User', models.DO_NOTHING)
    type = models.TextField()  # This field type is a guess.
    mode = models.TextField()  # This field type is a guess.
    comment_count = models.JSONField()
    last_updated_by = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'key_result'


class KeyResultCheckIn(models.Model):
    id = models.UUIDField(primary_key=True)
    value = models.FloatField()
    confidence = models.IntegerField()
    created_at = models.DateTimeField()
    key_result = models.ForeignKey(KeyResult, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)
    parent = models.OneToOneField('self', models.DO_NOTHING, blank=True, null=True)
    previous_state = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'key_result_check_in'


class KeyResultCheckMark(models.Model):
    id = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField()
    state = models.TextField()  # This field type is a guess.
    description = models.TextField()
    updated_at = models.DateTimeField()
    key_result = models.ForeignKey(KeyResult, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)
    assigned_user = models.ForeignKey('User', models.DO_NOTHING, related_name='keyresultcheckmark_assigned_user_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'key_result_check_mark'


class KeyResultComment(models.Model):
    id = models.UUIDField(primary_key=True)
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    key_result = models.ForeignKey(KeyResult, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)
    type = models.TextField()  # This field type is a guess.
    extra = models.TextField(blank=True, null=True)  # This field type is a guess.
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'key_result_comment'


class KeyResultSupportTeamMembersUser(models.Model):
    key_result = models.OneToOneField(KeyResult, models.DO_NOTHING, primary_key=True)  # The composite primary key (key_result_id, user_id) found, that is not supported. The first column is selected.
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'key_result_support_team_members_user'
        unique_together = (('key_result', 'user'),)


class KeyResultUpdate(models.Model):
    id = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField()
    key_result = models.ForeignKey(KeyResult, models.DO_NOTHING)
    author = models.JSONField()
    old_state = models.JSONField()
    patches = models.JSONField()
    new_state = models.JSONField()

    class Meta:
        managed = False
        db_table = 'key_result_update'


class Migrations(models.Model):
    timestamp = models.BigIntegerField()
    name = models.CharField()

    class Meta:
        managed = False
        db_table = 'migrations'


class Objective(models.Model):
    title = models.CharField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    cycle = models.ForeignKey(Cycle, models.DO_NOTHING)
    id = models.UUIDField(primary_key=True)
    owner = models.ForeignKey('User', models.DO_NOTHING)
    team = models.ForeignKey('Team', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(blank=True, null=True)
    mode = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'objective'


class Task(models.Model):
    id = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('User', models.DO_NOTHING)
    assigned_user = models.ForeignKey('User', models.DO_NOTHING, related_name='task_assigned_user_set', blank=True, null=True)
    description = models.TextField()
    state = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'task'


class Team(models.Model):
    name = models.CharField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    id = models.UUIDField(primary_key=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey('User', models.DO_NOTHING)
    gender = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'team'


class TeamUsersUser(models.Model):
    team = models.OneToOneField(Team, models.DO_NOTHING, primary_key=True)  # The composite primary key (team_id, user_id) found, that is not supported. The first column is selected.
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'team_users_user'
        unique_together = (('team', 'user'),)


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


class User(models.Model):
    authz_sub = models.CharField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    role = models.CharField(blank=True, null=True)
    picture = models.CharField(blank=True, null=True)
    id = models.UUIDField(primary_key=True)
    gender = models.TextField(blank=True, null=True)  # This field type is a guess.
    first_name = models.CharField()
    last_name = models.CharField(blank=True, null=True)
    nickname = models.CharField(blank=True, null=True)
    linked_in_profile_address = models.CharField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    email = models.TextField(unique=True)  # This field type is a guess.
    status = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'user'


class UserSetting(models.Model):
    id = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField()
    key = models.TextField()  # This field type is a guess.
    value = models.CharField()
    user = models.ForeignKey(User, models.DO_NOTHING)
    updated_at = models.DateTimeField()
    preferences = models.JSONField()

    class Meta:
        managed = False
        db_table = 'user_setting'
