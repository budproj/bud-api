from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class Cycle(BaseModel):
    date_start: datetime
    date_end: datetime
    team: str
    period: str
    cadence: str
    parent: Optional[str]
    active: bool
    id: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]


class CycleDate(BaseModel):
    year: str
    quarter: str
