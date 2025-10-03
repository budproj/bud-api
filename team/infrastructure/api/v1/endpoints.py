from typing import List
from ninja import Router

from team.application.interfaces import ITeamApplicationService
from team.application.services import TeamApplicationService
from team.domain.entities import Team

team_router = Router(tags=["team"])
team_service: ITeamApplicationService = TeamApplicationService()

@team_router.get("/company/{company_id}", response={200: List[Team], 404: dict})
def get_list_company_teams(request, company_id: str):
    data = team_service.get_team_by_company_id(company_id)
    return data
