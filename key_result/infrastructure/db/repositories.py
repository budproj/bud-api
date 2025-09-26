from typing import List, Optional

from key_result.infrastructure.db.mappers import map_key_result_orm_to_entity
from key_result.application.interfaces import IKeyResultRepository
from key_result.domain.entities import KeyResult
from key_result.models import KeyResultORM


class DjangoKeyResultRepository(IKeyResultRepository):
    def find_by_team_id(self, team_id: str, filters) -> Optional[List[KeyResult]]:
        try:
            kr_orm = KeyResultORM.objects.filter(team__id=team_id, objective__cycle__active=True)
            kr_orm = filters.filter(kr_orm)
            return [map_key_result_orm_to_entity(i) for i in kr_orm]
        except KeyResultORM.DoesNotExist:
            return None
        
    def update_key_result(self, key_result_id: str, data: KeyResult) -> KeyResult | None:
        try:
            kr_orm = KeyResultORM.objects.get(id=key_result_id)
        except KeyResultORM.DoesNotExist:
            return None

        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(kr_orm, key, value)

        kr_orm.save()
        return map_key_result_orm_to_entity(kr_orm)
    
    def get_one(self, key_result_id: str) -> KeyResult | None:
        try:
            kr_orm = KeyResultORM.objects.get(id=key_result_id)
        except KeyResultORM.DoesNotExist:
            return None        
        return map_key_result_orm_to_entity(kr_orm)
