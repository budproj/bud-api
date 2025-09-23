from typing import List, Optional
from team.application.interfaces import ITeamRepository
from team.domain.entities import Team
from team.infrastructure.db.mappers import map_team_orm_to_entity
from team.models import TeamCompany, TeamORM


class DjangoTeamRepository(ITeamRepository):
    def list_teams_by_company_id(self, company_id: str) -> Optional[List[Team]]:
        company_entity = self.get_company_from_team_id(company_id)
        try:
            if company_entity: 
                company_orm = TeamCompany.objects.filter(company_id=company_entity.id).select_related("team")
            else: 
                company_orm = TeamCompany.objects.filter(company_id=company_id).select_related("team")
            return [map_team_orm_to_entity(i.team) for i in company_orm]
        except TeamCompany.DoesNotExist:
            return None
        
    def get_company_from_team_id(self, team_id: str) -> Optional[Team]:
        try:
            team_orm = TeamCompany.objects.get(team_id=team_id)
            return map_team_orm_to_entity(team_orm.company)
        except TeamCompany.DoesNotExist:
            return None
        
    def get_team_from_id(self, team_id):
        try:
            team_orm = TeamORM.objects.get(team_id=team_id)
            return map_team_orm_to_entity(team_orm)
        except TeamORM.DoesNotExist:
            return None

    def check_user_in_team(self, team_id, user_id):
        try:
            team_orm = TeamORM.objects.get(team_id=team_id)
            return team_orm.users.filter(id=user_id).exists()
        except TeamORM.DoesNotExist:
            return None
        