from typing import Optional, List

from cycle.application.interfaces import ICycleApplicationService, ICycleRepository
from cycle.domain.entities import CycleDate
from cycle.infrastructure.db.repositories import DjangoCycleRepository
from team.infrastructure.db.repositories import DjangoTeamRepository


class CycleApplicationService(ICycleApplicationService):
    def __init__(self, cycle_repository: ICycleRepository = None):
        self.cycle_repository = cycle_repository or DjangoCycleRepository()
        self.team_repository = DjangoTeamRepository()
    
    def get_cycle_by_team_id(self, team_id):
        team_entity = self.team_repository.get_company_from_team_id(team_id)
        if team_entity:
            return self.cycle_repository.find_cycle_by_team_id(team_entity.id)
        return [], 404, {'error': 'Wrong input: Team do not exist.'}

    def get_cycle_date_by_team_id(self, team_id) -> Optional[List[CycleDate]]:
        return self.cycle_repository.find_cycle_dates_by_team_id(team_id)
