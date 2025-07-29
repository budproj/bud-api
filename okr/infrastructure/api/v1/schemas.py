from datetime import datetime
from decimal import Decimal
from typing import Dict, List, Optional
from ninja import Schema

class KeyResultOut(Schema):
    type: str
    mode: str
    title: str
    owner: str
    format: str
    objective: str
    comment_count: Dict[str, int]
    goal: Decimal
    initial_value: Decimal
    id: Optional[str] = None
    team: Optional[str] = None
    description: Optional[str] = None
    last_updated_by: Optional[Dict[str, str]] = None
    support_team: List[str]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None