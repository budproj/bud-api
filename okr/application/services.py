from typing import Optional, List

from okr.application.interfaces import IKeyResultApplicationService
from okr.domain.entities import KeyResult
from okr.infrastructure.db.repositories import DjangoKeyResultRepository, IKeyResultRepository


class KeyResultApplicationService(IKeyResultApplicationService):
    def __init__(self, kr_repository: IKeyResultRepository = None):
        self.kr_repository = kr_repository or DjangoKeyResultRepository()
    
    def get_key_results_by_team_id(self, team_id) -> Optional[List[KeyResult]]:
        return self.kr_repository.find_by_team_id(team_id)