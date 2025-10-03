from pydantic import BaseModel
from typing import Optional, List

class TaskSummary(BaseModel):
    id: Optional[str]
    teamId: Optional[str]
    owner: Optional[str]
    ownerFullName: Optional[str]
    status: Optional[str]
    title: Optional[str]
    description: Optional[str]
    priority: int
    supportTeam: Optional[List[str]]