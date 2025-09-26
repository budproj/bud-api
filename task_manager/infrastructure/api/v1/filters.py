import re
from datetime import timedelta

from ninja import FilterSchema, Field
from typing import Optional

from django.db.models import Q
from django.utils import timezone

from api.utils.translate_datetime import TranslateRelativeDate
import key_result
from task_manager.models import TaskORM

def exclude_string_spaces(text: str):
    if ' ' in text:
        return text.replace(' ', '')
    return text

class TasksFilterSchema(FilterSchema):
    team_id: Optional[str] = Field(None, q='team_id')
    key_result_id: Optional[str] = Field(None, q='key_result_id')
    deleted_at: Optional[bool] = Field(None, q='deleted_at')
    show_done: Optional[str] = Field(None, q='show_done')
    cy: Optional[str] = Field(None, q='cy')
    
    def filter_key_result_id(self, value: str):
        if value == '' or value is None:
            return Q()
        if value == 'empty':
            return Q(key_result_id__isnull=True)
        return Q(key_result_id=value)
    
    def filter_team_id(self, value: str):
        if value == '' or value is None:
            return Q()
        return Q(team_id=value)
    
    def filter_deleted_at(self, value: str):
        if value == '' or value is None:
            return Q()
        return Q(deleted_at__isnull=bool(value))
    
    def filter_cy(self, value: str):
        if value == '' or value is None:
            return Q()
        
        cycle = value.split('+')
                 
        year = exclude_string_spaces(cycle[0])
        quarter = exclude_string_spaces(cycle[1]) if cycle[1] != '' else None
        if year == '' and quarter == '':
            return Q()
        return Q(cycle__id=quarter or year)
    
    def filter_show_done(self, value: str):
        if value == '' or value is None:
            return Q()
        
        date_range = None
        match value:
            case '1w':
                date_range = TranslateRelativeDate(
                    timezone, last='0 weeks', since=None, upto=None
                ).date_range
            case '2w':
                date_range = TranslateRelativeDate(
                    timezone, last='2 weeks', since=None, upto=None
                ).date_range
            case '4w':
                date_range = TranslateRelativeDate(
                    timezone, last='0 months', since=None, upto=None
                ).date_range
        
        if date_range:
            return ((Q(status=TaskORM.TaskStatusChoices.DONE) & Q(due_date__range=date_range)) | ~Q(status=TaskORM.TaskStatusChoices.DONE)) 
        return Q()