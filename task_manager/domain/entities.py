from datetime import datetime
from ninja import Field
from pydantic import BaseModel
from typing import List, Optional

from key_result.domain.entities import KeyResult
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
    supportTeam: Optional[List[str]] = None
    attachments: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    orderindex: Optional[int] = None
    id: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    deletedAt: Optional[datetime] = None

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
    supportTeam: Optional[List[str]]
    attachments: Optional[List[str]]
    tags: Optional[List[str]]
    orderindex: Optional[int]
    id: Optional[str]
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]
    deletedAt: Optional[datetime]
