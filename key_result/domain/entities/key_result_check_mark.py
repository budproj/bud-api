from datetime import datetime
from pydantic import BaseModel
from typing import Optional


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
