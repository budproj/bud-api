from datetime import datetime
from pydantic import BaseModel
from typing import Any, Dict, Optional


class KeyResultUpdate(BaseModel):
    key_result: str
    author: Dict[str, Any]
    old_state: Dict[str, Any]
    patches: Dict[str, Any]
    new_state: Dict[str, Any]
    id: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]
