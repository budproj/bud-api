from typing import Optional

from ninja import FilterSchema, Field
from django.db.models import Q

def exclude_string_spaces(text: str):
    if ' ' in text:
        return text.replace(' ', '')
    return text

class KeyResultFilterSchema(FilterSchema):
    cy: Optional[str] = Field(None, q='cy')
    
    def filter_cy(self, value: str):
        if value == '' or value is None:
            return Q()
        
        cycle = value.split('+')
                 
        year = exclude_string_spaces(cycle[0])
        quarter = exclude_string_spaces(cycle[1]) if cycle[1] != '' else None
        if year == '' and quarter == '':
            return Q()
        return Q(objective__cycle__id=quarter or year)