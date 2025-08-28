from datetime import datetime
from pydantic import BaseModel
from decimal import Decimal
from typing import Any, Dict, Optional, List


class Cycle(BaseModel):
    date_start: datetime
    date_end: datetime
    team: str
    period: str
    cadence: str
    parent: Optional[str]
    active: bool
    id: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]


class Objective(BaseModel):
    title: str
    cycle: str
    owner: str
    mode: str
    team: Optional[str]
    description: Optional[str]
    id: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]


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
    team: Optional[str]
    description: Optional[str]
    last_updated_by: Optional[Dict[str, str]]
    support_team: List[str]
    id: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]


class KeyResultCheckIn(BaseModel):
    value: Decimal
    confidence: int
    key_result: str
    user: str
    id: Optional[str]
    comment: Optional[str]
    parent: Optional[str]
    previous_state: Optional[Dict[str, Any]]
    id: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]


class KeyResultCheckMark(BaseModel):
    state: str
    description: str
    key_result: str
    user: str
    assigned_user: Optional[str]
    id: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]


class KeyResultSupportTeamMembersUser(BaseModel):
    key_result: Optional[str]
    user: Optional[str]


class KeyResultUpdateORM(BaseModel):
    key_result: str
    author: Dict[str, Any]
    old_state: Dict[str, Any]
    patches: Dict[str, Any]
    new_state: Dict[str, Any]
    id: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]


class CycleDate(BaseModel):
    year: str
    quarter: str
