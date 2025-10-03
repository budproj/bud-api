from django.db import models

from api.models import BaseModel


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
    objective = models.ForeignKey('objective.ObjectiveORM', models.CASCADE)
    team = models.ForeignKey('team.TeamORM', models.CASCADE, blank=True, null=True)
    owner = models.ForeignKey('user.UserORM', models.CASCADE)
    type = models.TextField(choices=KeyResultTypeChoices.choices)
    mode = models.TextField(choices=KeyResultModeChoices.choices)
    comment_count = models.JSONField()
    last_updated_by = models.JSONField(blank=True, null=True)
    support_team = models.ManyToManyField('user.UserORM', through='KeyResultSupportTeamMembersUserORM', related_name='suport_team_key_result')

    class Meta:
        db_table = 'key_result'
        managed = False


class KeyResultCheckInORM(BaseModel):
    value = models.FloatField()
    confidence = models.IntegerField()
    key_result = models.ForeignKey('key_result.KeyResultORM', models.CASCADE)
    user = models.ForeignKey('user.UserORM', models.CASCADE)
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
    key_result = models.ForeignKey('key_result.KeyResultORM', models.CASCADE)
    user = models.ForeignKey('user.UserORM', models.CASCADE)
    assigned_user = models.ForeignKey('user.UserORM', models.CASCADE, related_name='assigned_user_set', blank=True, null=True)

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
    key_result = models.ForeignKey('key_result.KeyResultORM', models.CASCADE)
    user = models.ForeignKey('user.UserORM', models.CASCADE)
    type = models.TextField(choices=KeyResultCommentTypeChoices.choices)
    extra = models.TextField(blank=True, null=True) 
    parent = models.ForeignKey('self', models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'key_result_comment'
        managed = False


class KeyResultSupportTeamMembersUserORM(models.Model):
    key_result = models.ForeignKey('key_result.KeyResultORM', models.DO_NOTHING, null=True, blank=True)
    user = models.ForeignKey('user.UserORM', models.DO_NOTHING, null=True, blank=True)

    class Meta:
        db_table = 'key_result_support_team_members_user'
        managed = False


class KeyResultUpdateORM(BaseModel):
    key_result = models.ForeignKey('key_result.KeyResultORM', models.DO_NOTHING)
    author = models.JSONField()
    old_state = models.JSONField()
    patches = models.JSONField()
    new_state = models.JSONField()

    class Meta:
        db_table = 'key_result_update'
        managed = False
