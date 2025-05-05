from django.db import models

from api.base.base_model import BaseModel
from team.models import Team
from user.models import User

from okr.enums.cycle_choices import CycleCadenceChoices
from okr.enums.objective_choices import ObjectiveModeChoices
from okr.enums.key_result_choices import (
    KeyResultFormatChoices,
    KeyResultTypeChoices,
    KeyResultModeChoices,
)
from okr.enums.key_result_check_mark_choices import KeyResultCheckMarkStateChoices
from okr.enums.key_result_comment_choices import KeyResultCommentTypeChoices


class Cycle(BaseModel):
    date_start = models.DateTimeField() # initial
    date_end = models.DateTimeField() # initial
    team = models.ForeignKey(Team, models.CASCADE) # initial
    period = models.CharField() # initial
    cadence = models.TextField(choices=CycleCadenceChoices.choices) # initial
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True) # initial
    active = models.BooleanField() # initial

    class Meta:
        db_table = 'cycle'


class Objective(BaseModel):
    title = models.CharField() # initial
    cycle = models.ForeignKey(Cycle, models.CASCADE) # initial
    owner = models.ForeignKey(User, models.CASCADE) # initial
    team = models.ForeignKey(Team, models.CASCADE, blank=True, null=True) # initial
    description = models.CharField(blank=True, null=True) # initial
    mode = models.TextField(choices=ObjectiveModeChoices.choices) # initial

    class Meta:
        db_table = 'objective'


class KeyResult(BaseModel):
    title = models.CharField() # initial
    goal = models.DecimalField(max_digits=14, decimal_places=2) # initial
    initial_value = models.DecimalField(max_digits=14, decimal_places=2) # initial
    description = models.TextField(blank=True, null=True) # initial
    format = models.TextField(choices=KeyResultFormatChoices.choices) # initial
    objective = models.ForeignKey(Objective, models.CASCADE) # initial
    team = models.ForeignKey(Team, models.CASCADE, blank=True, null=True) # initial
    owner = models.ForeignKey(User, models.CASCADE) # initial
    type = models.TextField(choices=KeyResultTypeChoices.choices) # initial
    mode = models.TextField(choices=KeyResultModeChoices.choices) # initial
    comment_count = models.JSONField() # initial
    last_updated_by = models.JSONField(blank=True, null=True) # initial
    support_team = models.ManyToManyField(User, through='KeyResultSupportTeamMembersUser', related_name='suport_team_key_result') # initial

    class Meta:
        db_table = 'key_result'


class KeyResultCheckIn(BaseModel):
    value = models.FloatField() # initial
    confidence = models.IntegerField() # initial
    key_result = models.ForeignKey(KeyResult, models.CASCADE) # initial
    user = models.ForeignKey(User, models.CASCADE) # initial
    comment = models.TextField(blank=True, null=True) # initial
    parent = models.OneToOneField('self', models.DO_NOTHING, blank=True, null=True) # initial
    previous_state = models.JSONField(blank=True, null=True) # initial

    class Meta:
        db_table = 'key_result_check_in'


class KeyResultCheckMark(BaseModel):
    state = models.TextField(choices=KeyResultCheckMarkStateChoices.choices) # initial
    description = models.TextField() # initial
    key_result = models.ForeignKey(KeyResult, models.CASCADE) # initial
    user = models.ForeignKey(User, models.CASCADE) # initial
    assigned_user = models.ForeignKey(User, models.CASCADE, related_name='assigned_user_set', blank=True, null=True) # initial

    class Meta:
        db_table = 'key_result_check_mark'


class KeyResultComment(BaseModel):
    text = models.TextField(blank=True, null=True) # initial
    key_result = models.ForeignKey(KeyResult, models.CASCADE) # initial
    user = models.ForeignKey(User, models.CASCADE) # initial
    type = models.TextField(choices=KeyResultCommentTypeChoices.choices) # initial
    extra = models.TextField(blank=True, null=True)  # initial
    parent = models.ForeignKey('self', models.CASCADE, blank=True, null=True) # initial

    class Meta:
        db_table = 'key_result_comment'


class KeyResultSupportTeamMembersUser(models.Model):
    key_result = models.ForeignKey(KeyResult, models.DO_NOTHING, null=True, blank=True) # initial
    user = models.ForeignKey(User, models.DO_NOTHING, null=True, blank=True) # initial

    class Meta:
        db_table = 'key_result_support_team_members_user'


class KeyResultUpdate(BaseModel):
    key_result = models.ForeignKey(KeyResult, models.DO_NOTHING) # initial
    author = models.JSONField() # initial
    old_state = models.JSONField() # initial
    patches = models.JSONField() # initial
    new_state = models.JSONField() # initial

    class Meta:
        db_table = 'key_result_update'
