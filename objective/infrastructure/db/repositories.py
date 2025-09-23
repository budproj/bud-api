from typing import List, Optional

import objective
from objective.infrastructure.db.mappers import map_objective_orm_to_entity
from objective.application.interfaces import IObjectiveRepository
from objective.domain.entities import Objective
from objective.models import ObjectiveORM
    

class DjangoObjectiveRepository(IObjectiveRepository):
    def patch_objective(self, objective_id: str, data: Objective) -> Optional[Objective]:
        try:
            objective_orm = ObjectiveORM.objects.get(id=objective_id)
        except ObjectiveORM.DoesNotExist:
            return None

        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(objective_orm, key, value)

        objective_orm.save()
        return map_objective_orm_to_entity(objective_orm)
    
    def select_objective_by_team_id(self, team_id: str) -> Optional[List[Objective]]:
        objective_orm = ObjectiveORM.objects.filter(team__id=team_id, cycle__active=True)
        return [map_objective_orm_to_entity(i) for i in objective_orm]
