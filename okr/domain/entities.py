from datetime import date
from pydantic import BaseModel
from decimal import Decimal
from typing import Optional, List


class KeyResult(BaseModel):
    type: str
    mode: str
    title: str
    owner: str
    format: str
    objective: str
    comment_count: str
    goal: Decimal
    initial_value: Decimal
    id: Optional[str] = None
    team: Optional[str] = None
    description: Optional[str] = None
    last_updated_by: Optional[List[str]] = None
    support_team: List[str]
    created_at: Optional[date] = None
    updated_at: Optional[date] = None
    deleted_at: Optional[date] = None

