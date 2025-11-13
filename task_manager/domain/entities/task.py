from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

from user.domain.entities import User


class Task(BaseModel):
    team: Optional[str] = None
    keyResult: Optional[str] = None
    cycle: Optional[str] = None
    owner: Optional[str] = None
    status: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[int] = None
    initialDate: Optional[datetime] = None
    dueDate: Optional[datetime] = None
    supportTeam: Optional[List[User]] = None
    attachments: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    orderindex: Optional[int] = None
    id: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    deletedAt: Optional[datetime] = None
