from datetime import datetime
from pydantic import BaseModel
from decimal import Decimal
from typing import Any, Dict, Optional, List


class KeyResultCheckIn(BaseModel):
    value: Decimal
    confidence: int
    key_result: str
    user: str
    id: Optional[str]
    comment: Optional[str]
    parent: Optional['KeyResultCheckIn']
    previous_state: Optional[Dict[str, Any]]
    
    
class KeyResult(BaseModel):
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


class Cycle(BaseModel):
    date_start: datetime
    date_end: datetime
    team: str
    period: str
    cadence: str
    parent: Optional['Cycle']
    active: bool
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None


class CycleDate(BaseModel):
    year: str
    quarter: str