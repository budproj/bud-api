from datetime import datetime
from pydantic import BaseModel
from decimal import Decimal
from typing import Any, Dict, Optional


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
