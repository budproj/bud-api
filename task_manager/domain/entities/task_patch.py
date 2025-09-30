from datetime import datetime
from ninja import Field
from pydantic import BaseModel
from typing import List, Optional


class TaskPatch(BaseModel):
    team: Optional[str] = None
    key_result_id: Optional[str] = Field(None, alias='keyResult')
    cycle: Optional[str] = None
    owner: Optional[str] = None
    status: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[int] = None
    initial_date: Optional[datetime] = Field(None, alias='initialDate')
    due_date: Optional[datetime] = Field(None, alias='dueDate')
    support_team: Optional[List[str]] = Field(None, alias='supportTeam')
    attachments: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    orderindex: Optional[int] = None
    id: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    deletedAt: Optional[datetime] = None