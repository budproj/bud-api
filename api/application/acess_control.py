from abc import ABC, abstractmethod
from typing import Tuple

from api.application.policy_adapter import PolicyAdapter
from team.infrastructure.db.repositories import DjangoTeamRepository
from user.domain.entities import UserWithContext
from api.application.types import Resource, Command, Scope


class AccessControl(ABC):
    resource: Resource
    policy_adapter: PolicyAdapter = PolicyAdapter()
    team_repository = DjangoTeamRepository()
    
    def can_create(self, user: UserWithContext, *args) -> bool:
        return self.resolve_context_command_cermission(Command.CREATE, user, *args)

    def can_read(self, user: UserWithContext, *args) -> bool:
        return self.resolve_entity_command_permission(Command.READ, user, *args)

    def can_update(self, user: UserWithContext, *args) -> bool:
        return self.resolve_entity_command_permission(Command.UPDATE, user, *args)

    def can_delete(self, user: UserWithContext, *args) -> bool:
        return self.resolve_entity_command_permission(Command.DELETE, user, *args)
    
    def is_company_member(self, team_id: str, user_id: str) -> bool:
        team = self.team_repository.get_company_from_team_id(team_id)
        if team and team.owner:
            return team.owner.id == user_id
        return False
    
    def resolve_context_command_cermission(self, command: Command, user: UserWithContext, *args) -> bool:
        is_owner, is_team_leader, is_company_member = self.resolve_context_scopes(user, *args)
        return self.can_activate(user, command, is_owner, is_team_leader, is_company_member)
    
    def resolve_entity_command_permission(self, command: Command, user: UserWithContext, *args) -> bool:
        is_owner, is_team_leader, is_company_member = self.resolve_entity_scopes(user, *args)
        return self.can_activate(user, command, is_owner, is_team_leader, is_company_member)
    
    def can_activate(self, user: UserWithContext, command: Command, owns: bool, team: bool, company: bool) -> bool:
        required_permissions = self.get_permissions_for_scopes(command, owns, team, company)
        return len([permission for permission in required_permissions if permission in user.token.permissions]) > 0
        
    def get_permissions_for_scopes(self, command: Command, owns: bool, team: bool, company: bool) -> list[str]:
        permissions = [
            owns and self.policy_adapter.build_permission(self.resource, command, Scope.OWNS),
            team and self.policy_adapter.build_permission(self.resource, command, Scope.TEAM),
            company and self.policy_adapter.build_permission(self.resource, command, Scope.COMPANY),
            self.policy_adapter.build_permission(self.resource, command, Scope.ANY),
        ]
        return [permission for permission in permissions if bool(permission)]

    @abstractmethod
    def resolve_context_scopes(self, user: UserWithContext, *args) -> Tuple[bool, bool, bool]:
        pass
    
    @abstractmethod
    def resolve_entity_scopes(self, user: UserWithContext, *args) -> Tuple[bool, bool, bool]:
        pass