from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class TaskComments(BaseModel):
    userId: Optional[str]
    taskId: Optional[str]
    id: Optional[str]
    text: Optional[str]
    parentId: Optional[str]
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]
    deletedAt: Optional[datetime]