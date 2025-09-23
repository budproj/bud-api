from datetime import datetime
from pydantic import BaseModel
from typing import Optional, Dict

from api.application.types import Effect, Resource, Command, Scope


class User(BaseModel):
    id: Optional[str]
    authz_sub: str
    role: Optional[str]
    picture: Optional[str]
    gender: Optional[str]
    first_name: str
    last_name: Optional[str]
    nickname: Optional[str]
    linked_in_profile_address: Optional[str]
    about: Optional[str]
    email: str
    status: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]


class UserSetting(BaseModel):
    key: str
    value: str
    user: User
    preferences: Dict[str, str]


class AuthzData(BaseModel):
    iss: str
    sub: str
    azp: str
    scope: str
    aud: list[str]
    iat: int
    exp: int
    permissions: list[str]



class UserWithContext(User):
    token: AuthzData
    resourcePolicy: Dict[Resource, Dict[Command, Dict[Scope, Effect]]]

class AccessControlScopes(BaseModel):
    is_owner: bool
    is_team_leader: bool
    is_company_member: bool