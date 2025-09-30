from pydantic import BaseModel
from typing import Optional


class KeyResultSupportTeamMembersUser(BaseModel):
    key_result: Optional[str]
    user: Optional[str]
