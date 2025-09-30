from pydantic import BaseModel
from typing import Dict, Optional, List
from decimal import Decimal
from datetime import datetime


class KeyResult(BaseModel):
    type: Optional[str] = None
    mode: Optional[str] = None
    title: Optional[str] = None
    owner: Optional[str] = None
    format: Optional[str] = None
    objectiveId: Optional[str] = None
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
