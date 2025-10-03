from pydantic import BaseModel
from typing import Optional


class TaskHistory(BaseModel):
    task: str
    field: str
    old_state: Optional[str]
    new_state: Optional[str]
    author: Optional[str]