from typing import List, Optional

from cycle.infrastructure.db.mappers import map_cycle_orm_to_entity
from cycle.application.interfaces import ICycleRepository
from cycle.models import CycleORM
    
    
class DjangoCycleRepository(ICycleRepository):
    def find_cycle_by_team_id(self, team_id):
        cycle_orm = CycleORM.objects.filter(team__id=team_id, active=True)
        return [map_cycle_orm_to_entity(i) for i in cycle_orm], 200, None
        
    def find_all_cycles_by_team_id(self, team_id: str):
        cycle_orm = CycleORM.objects.filter(team__id=team_id)
        return [map_cycle_orm_to_entity(i) for i in cycle_orm], 200, None
    