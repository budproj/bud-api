from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class TaskComments(BaseModel):
    user: str
    task: str
    id: Optional[str]
    text: Optional[str]
    parent: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]