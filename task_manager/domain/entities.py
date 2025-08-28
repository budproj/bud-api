from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

from okr.domain.entities import KeyResult
from user.domain.entities import User


class Task(BaseModel):
    team: Optional[str]
    key_result: Optional[str]
    cycle: Optional[str]
    owner: Optional[str]
    status: Optional[str]
    title: Optional[str]
    description: Optional[str]
    priority: Optional[int]
    initial_date: Optional[datetime]
    due_date: Optional[datetime]
    support_team: Optional[List[str]]
    attachments: Optional[List[str]]
    tags: Optional[List[str]]
    orderindex: Optional[int]
    id: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]


class TaskComments(BaseModel):
    user: str
    task: str
    id: Optional[str]
    text: Optional[str]
    parent: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]


class TaskHistory(BaseModel):
    task: str
    field: str
    old_state: Optional[str]
    new_state: Optional[str]
    author: Optional[str]


class TaskBoard(BaseModel):
    history: List[TaskHistory]
    users_related: List[User]
    owner_full_name: str
    team: Optional[str]
    key_result: Optional[KeyResult]
    cycle: Optional[str]
    owner: Optional[str]
    status: Optional[str]
    title: Optional[str]
    description: Optional[str]
    priority: Optional[int]
    initial_date: Optional[datetime]
    due_date: Optional[datetime]
    support_team: Optional[List[str]]
    attachments: Optional[List[str]]
    tags: Optional[List[str]]
    orderindex: Optional[int]
    id: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]
