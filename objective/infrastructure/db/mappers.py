from objective.domain.entities import Objective
from objective.models import ObjectiveORM

    
def map_objective_orm_to_entity(obj_orm: ObjectiveORM) -> Objective:
    return Objective(
        title=obj_orm.title,  
        cycle=str(obj_orm.cycle.id),
        owner=str(obj_orm.owner.id),
        mode=obj_orm.mode,
        teamId=str(obj_orm.team.id) if obj_orm.team else None,
        description=obj_orm.description,
        id=str(obj_orm.id),
        created_at=obj_orm.created_at,
        updated_at=obj_orm.updated_at,
        deleted_at=obj_orm.deleted_at
    )
