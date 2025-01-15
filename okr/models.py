from django.db import models
from api.base.base_model import BaseModel
from okr.enums.cycle_choices import CycleCadenceChoices
from okr.enums.objective_choices import ObjectiveModeChoices
from okr.enums.key_result_choices import KeyResultFormatChoices, KeyResultTypeChoices, KeyResultModeChoices
from okr.enums.key_result_check_mark_choices import KeyResultCheckMarkStateChoices
from okr.enums.key_result_comment_choices import KeyResultCommentTypeChoices

class Cycle(BaseModel):
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    team = models.ForeignKey('Team', models.CASCADE)
    period = models.CharField()
    cadence = models.TextField(choices=CycleCadenceChoices)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField()

    class Meta:
        db_table = 'cycle'

class Objective(BaseModel):
    title = models.CharField()
    cycle = models.ForeignKey('Cycle', models.CASCADE)
    owner = models.ForeignKey('User', models.CASCADE)
    team = models.ForeignKey('Team', models.CASCADE, blank=True, null=True)
    description = models.CharField(blank=True, null=True)
    mode = models.TextField(choices=ObjectiveModeChoices)

    class Meta:
        db_table = 'objective'
        
class KeyResult(BaseModel):
    title = models.CharField()
    goal = models.DecimalField(max_digits=14, decimal_places=2)
    initial_value = models.DecimalField(max_digits=14, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    format = models.TextField(choices=KeyResultFormatChoices)
    objective = models.ForeignKey('Objective', models.CASCADE)
    team = models.ForeignKey('Team', models.CASCADE, blank=True, null=True)
    owner = models.ForeignKey('User', models.CASCADE)
    type = models.TextField(choices=KeyResultTypeChoices)
    mode = models.TextField(choices=KeyResultModeChoices)
    comment_count = models.JSONField()
    last_updated_by = models.JSONField(blank=True, null=True)

    class Meta:
        db_table = 'key_result'


class KeyResultCheckIn(BaseModel):
    value = models.FloatField()
    confidence = models.IntegerField()
    key_result = models.ForeignKey('KeyResult', models.CASCADE)
    user = models.ForeignKey('User', models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    parent = models.OneToOneField('self', models.DO_NOTHING, blank=True, null=True)
    previous_state = models.JSONField(blank=True, null=True)

    class Meta:
        db_table = 'key_result_check_in'


class KeyResultCheckMark(BaseModel):
    state = models.TextField(choices=KeyResultCheckMarkStateChoices)
    description = models.TextField()
    key_result = models.ForeignKey('KeyResult', models.CASCADE)
    user = models.ForeignKey('User', models.CASCADE)
    assigned_user = models.ForeignKey('User', models.CASCADE, related_name='assigned_user_set', blank=True, null=True)

    class Meta:
        db_table = 'key_result_check_mark'


class KeyResultComment(BaseModel):
    text = models.TextField(blank=True, null=True)
    key_result = models.ForeignKey(KeyResult, models.CASCADE)
    user = models.ForeignKey('User', models.CASCADE)
    type = models.TextField(choices=KeyResultCommentTypeChoices)
    extra = models.TextField(blank=True, null=True)  # TODO: identify motivation to this field
    parent = models.ForeignKey('self', models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'key_result_comment'


class KeyResultSupportTeamMembersUser(models.Model):
    key_result_id = models.OneToOneField(KeyResult, models.DO_NOTHING)
    user_id = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False # django does not work with tables without id, so we don't manage this table
        db_table = 'key_result_support_team_members_user'
        unique_together = (('key_result', 'user'),)


class KeyResultUpdate(BaseModel):
    key_result = models.ForeignKey(KeyResult, models.DO_NOTHING)
    author = models.JSONField()
    old_state = models.JSONField()
    patches = models.JSONField()
    new_state = models.JSONField()

    class Meta:
        db_table = 'key_result_update'