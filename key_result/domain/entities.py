from datetime import datetime
from pydantic import BaseModel
from decimal import Decimal
from typing import Any, Dict, Optional, List
from ninja import Field, Schema


class KeyResult(BaseModel):
    type: Optional[str] = None
    mode: Optional[str] = None
    title: Optional[str] = None
    owner: Optional[str] = None
    format: Optional[str] = None
    objective_id: Optional[str] = Field(None, alias="objectiveId")
    comment_count: Optional[Dict[str, int]] = None
    goal: Optional[Decimal] = None
    initial_value: Optional[Decimal] = None
    team: Optional[str] = None
    description: Optional[str] = None
    last_updated_by: Optional[Dict[str, str]] = None
    support_team: Optional[List[str]] = None
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

    class Config:
        populate_by_name = True

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
