from typing import Optional, List

from okr.application.interfaces import ICycleApplicationService, ICycleRepository, IKeyResultApplicationService, ITeamRepository, \
    IKeyResultRepository
from okr.domain.entities import Cycle, CycleDate, KeyResult
from okr.infrastructure.db.repositories import DjangoCycleRepository, DjangoKeyResultRepository, DjangoCompanyRepository


class KeyResultApplicationService(IKeyResultApplicationService):
    def __init__(self, kr_repository: IKeyResultRepository = None):
        self.kr_repository = kr_repository or DjangoKeyResultRepository()
    
    def get_key_results_by_team_id(self, team_id) -> Optional[List[KeyResult]]:
        return self.kr_repository.find_by_team_id(team_id)

class CycleApplicationService(ICycleApplicationService):
    def __init__(self, cycle_repository: ICycleRepository = None):
        self.cycle_repository = cycle_repository or DjangoCycleRepository()
        self.team_repository = DjangoCompanyRepository()
    
    def get_cycle_by_team_id(self, team_id) -> Optional[List[Cycle]]:
        company_id = self.team_repository.find_team_company_by_id(team_id)
        return self.cycle_repository.find_cycle_by_team_id(company_id)

    def get_cycle_date_by_team_id(self, team_id) -> Optional[List[CycleDate]]:
        return self.cycle_repository.find_cycle_dates_by_team_id(team_id)

