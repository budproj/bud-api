from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

from key_result.domain.entities.key_result import KeyResult
from task_manager.domain.entities.task_history import TaskHistory
from user.domain.entities import User


class TaskBoard(BaseModel):
    history: List[TaskHistory] 
    usersRelated: List[User]
    ownerFullName: str 
    team: Optional[str]
    keyResult: Optional[KeyResult]
    cycle: Optional[str]
    owner: Optional[str]
    status: Optional[str]
    title: Optional[str]
    description: Optional[str]
    priority: Optional[int]
    initialDate: Optional[datetime]
    dueDate: Optional[datetime]
    supportTeam: Optional[List[User]]
    attachments: Optional[List[str]]
    tags: Optional[List[str]]
    orderindex: Optional[int]
    id: Optional[str]
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]
    deletedAt: Optional[datetime]