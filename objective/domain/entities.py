from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional


class Objective(BaseModel):
    title: Optional[str] = None
    cycle_id: Optional[str] = Field(None, alias="cycleId")
    owner: Optional[str] = None
    mode: Optional[str] = None
    team_id: Optional[str] = Field(None, alias="teamId")
    description: Optional[str] = None
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
