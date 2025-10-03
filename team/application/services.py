from typing import List, Optional
from team.application.interfaces import ITeamApplicationService
from team.domain.entities import Team
from team.infrastructure.db.repositories import DjangoTeamRepository


class TeamApplicationService(ITeamApplicationService):
    def __init__(self):
        self.team_repository = DjangoTeamRepository()
    
    def get_team_by_company_id(self, company_id) -> Optional[List[Team]]:
        return self.team_repository.list_teams_by_company_id(company_id)
