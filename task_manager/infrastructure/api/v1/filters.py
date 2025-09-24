import re
from datetime import timedelta

from ninja import FilterSchema, Field
from typing import Optional

from django.db.models import Q
from django.utils import timezone

from api.utils.translate_datetime import TranslateRelativeDate


class TasksFilterSchema(FilterSchema):
    team_id: Optional[str] = Field(None, q='team__id')
    key_result_id: Optional[str] = Field(None, q='key_result__id')
    deleted_at: Optional[bool] = Field(None, q='deleted_at__isnull')
    show_done: Optional[bool] = Field(None, q='show_done')
    cy: Optional[str] = Field(None, q='cy')
    
    def filter_cy(self, value: str):
        if value is None:
            return None
        cycle = value.split('+')
                 
        year = int(cycle[0])
        quarter = int(cycle[1]) if bool(re.search(r'\d', cycle[1])) else None

        date_start = timezone.datetime(year, ((quarter or 1)-1)*3+1, 1)
        date_end = timezone.datetime(year, (quarter or 4)*3, 1)
        
        date_start -= timedelta(days=1)
        return Q(cycle__date_start__range=(date_start, date_end))
    
    def filter_show_done(self, value: str):
        if value is None:
            return None
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
            return Q(due_date__range=date_range)
        return Q()