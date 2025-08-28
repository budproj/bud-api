from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List

from user.domain.entities import User


class Team(BaseModel):
    name: str
    gender: str
    description: Optional[str]
    parent: Optional[str]
    owner: Optional[User]
    users: List[str]
    id: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]


class TeamUsersUser(BaseModel):
    team: Team
    user: User