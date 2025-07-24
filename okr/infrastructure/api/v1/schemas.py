from datetime import date
from decimal import Decimal
from ninja import Schema

class KeyResultOut(Schema):
    type: str
    mode: str
    title: str
    owner: str
    format: str
    objective: str
    comment_count: str
    goal: Decimal
    initial_value: Decimal
    id: str
    team: str
    description: str
    last_updated_by: str
    support_team: str
    created_at: date
    updated_at: date
    deleted_at: date