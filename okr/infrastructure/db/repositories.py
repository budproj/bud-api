from typing import List, Optional

from okr.infrastructure.db.mappers import map_key_result_orm_to_entity
from okr.application.interfaces import IKeyResultRepository
from okr.domain.entities import KeyResult
from okr.models import KeyResultORM


class DjangoKeyResultRepository(IKeyResultRepository):
    def find_by_team_id(self, team_id: str) -> Optional[List[KeyResult]]:
        try:
            kr_orm = KeyResultORM.objects.filter(team__id=team_id, objective__cycle__active=True)
            return [map_key_result_orm_to_entity(i) for i in kr_orm]
        except KeyResultORM.DoesNotExist:
            return None