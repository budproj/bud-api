from django.db import models

from api.models import BaseModel
from team.models import TeamORM
from user.models import UserORM


class CycleORM(BaseModel):
    class CycleCadenceChoices(models.TextChoices):
        YEARLY = 'YEARLY'
        QUARTERLY = 'QUARTERLY'
    
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    team = models.ForeignKey(TeamORM, models.CASCADE)
    period = models.CharField()
    cadence = models.TextField(choices=CycleCadenceChoices.choices)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField()

    class Meta:
        db_table = 'cycle'
        managed = False


class ObjectiveORM(BaseModel):
    class ObjectiveModeChoices(models.TextChoices):
        COMPLETED = 'COMPLETED'
        PUBLISHED = 'PUBLISHED'
        DRAFT = 'DRAFT'
        DELETED = 'DELETED'
    
    title = models.CharField()
    cycle = models.ForeignKey('okr.CycleORM', models.CASCADE)
    owner = models.ForeignKey(UserORM, models.CASCADE)
    team = models.ForeignKey(TeamORM, models.CASCADE, blank=True, null=True)
    description = models.CharField(blank=True, null=True)
    mode = models.TextField(choices=ObjectiveModeChoices.choices)

    class Meta:
        db_table = 'objective'
        managed = False


class KeyResultORM(BaseModel):
    class KeyResultTypeChoices(models.TextChoices):
        ASCENDING = 'ASCENDING'
        DESCENDING = 'DESCENDING'
    
    class KeyResultFormatChoices(models.TextChoices):
        NUMBER = 'NUMBER'
        PERCENTAGE = 'PERCENTAGE'
        COIN_BRL = 'COIN_BRL'
        COIN_USD = 'COIN_USD'
        COIN_EUR = 'COIN_EUR'
        COIN_GBP = 'COIN_GBP'
    
    class KeyResultModeChoices(models.TextChoices):
        COMPLETED = 'COMPLETED'
        PUBLISHED = 'PUBLISHED'
        DRAFT = 'DRAFT'
        DELETED = 'DELETED'

    title = models.CharField()
    goal = models.DecimalField(max_digits=14, decimal_places=2)
    initial_value = models.DecimalField(max_digits=14, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    format = models.TextField(choices=KeyResultFormatChoices.choices)
    objective = models.ForeignKey(ObjectiveORM, models.CASCADE)
    team = models.ForeignKey(TeamORM, models.CASCADE, blank=True, null=True)
    owner = models.ForeignKey(UserORM, models.CASCADE)
    type = models.TextField(choices=KeyResultTypeChoices.choices)
    mode = models.TextField(choices=KeyResultModeChoices.choices)
    comment_count = models.JSONField()
    last_updated_by = models.JSONField(blank=True, null=True)
    support_team = models.ManyToManyField(UserORM, through='KeyResultSupportTeamMembersUserORM', related_name='suport_team_key_result')

    class Meta:
        db_table = 'key_result'
        managed = False


class KeyResultCheckInORM(BaseModel):
    value = models.FloatField()
    confidence = models.IntegerField()
    key_result = models.ForeignKey('okr.KeyResultORM', models.CASCADE)
    user = models.ForeignKey(UserORM, models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    parent = models.OneToOneField('self', models.DO_NOTHING, blank=True, null=True)
    previous_state = models.JSONField(blank=True, null=True)

    class Meta:
        db_table = 'key_result_check_in'
        managed = False


class KeyResultCheckMarkORM(BaseModel):
    class KeyResultCheckMarkStateChoices(models.TextChoices):
        CHECKED = 'CHECKED'
        UNCHECKED = 'UNCHECKED'
    state = models.TextField(choices=KeyResultCheckMarkStateChoices.choices)
    description = models.TextField()
    key_result = models.ForeignKey('okr.KeyResultORM', models.CASCADE)
    user = models.ForeignKey(UserORM, models.CASCADE)
    assigned_user = models.ForeignKey(UserORM, models.CASCADE, related_name='assigned_user_set', blank=True, null=True)

    class Meta:
        db_table = 'key_result_check_mark'
        managed = False


class KeyResultCommentORM(BaseModel):
    class KeyResultCommentTypeChoices(models.TextChoices):
        SUGGESTION = 'suggestion'
        PRAISAL = 'praisal'
        QUESTION = 'question'
        ALIGNMENT = 'alignment'
        IMPROVEMENT = 'improvement'
        ISSUE = 'issue'
        COMMENT = 'comment'
        
    text = models.TextField(blank=True, null=True)
    key_result = models.ForeignKey('okr.KeyResultORM', models.CASCADE)
    user = models.ForeignKey(UserORM, models.CASCADE)
    type = models.TextField(choices=KeyResultCommentTypeChoices.choices)
    extra = models.TextField(blank=True, null=True) 
    parent = models.ForeignKey('self', models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'key_result_comment'
        managed = False


class KeyResultSupportTeamMembersUserORM(models.Model):
    key_result = models.ForeignKey('okr.KeyResultORM', models.DO_NOTHING, null=True, blank=True)
    user = models.ForeignKey(UserORM, models.DO_NOTHING, null=True, blank=True)

    class Meta:
        db_table = 'key_result_support_team_members_user'
        managed = False


class KeyResultUpdateORM(BaseModel):
    key_result = models.ForeignKey('okr.KeyResultORM', models.DO_NOTHING)
    author = models.JSONField()
    old_state = models.JSONField()
    patches = models.JSONField()
    new_state = models.JSONField()

    class Meta:
        db_table = 'key_result_update'
        managed = False
