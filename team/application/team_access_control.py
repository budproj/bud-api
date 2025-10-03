from typing import Tuple, List

from api.application.acess_control import AccessControl
from api.application.types import Resource
from team.domain.entities import Team
from user.domain.entities import UserWithContext

class TeamAccessControl(AccessControl):
    resource = Resource.TEAM

    def is_team_owner(self, user: UserWithContext, team: Team) -> bool:
        return user.id == team.owner.id

    """
    def resolve_context_scopes(self, user: UserWithContext, parentTeamID: str, *args) -> Tuple[bool, bool, bool]:
        team, teams, company = self.get_context_related_entities(parentTeamID)
        isTeamLeader = self.isTeamLeader(teams, user)
        isCompanyMember = self.isCompanyMember([company], user)
        isOwner = team.owner.id == user.id
        return isOwner, isTeamLeader, isCompanyMember

    def get_context_related_entities(self, team_id: str) -> Tuple[Team, List[Team], Team]:
        team = self.core.dispatchCommand<Team>('get-team', teamIndexes)
        teams = self.core.dispatchCommand<Team[]>('get-team-tree', teamIndexes)
        company = this.core.dispatchCommand<Team>('get-team-company', team)

        return team, teams, company
    """
