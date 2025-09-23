from key_result.domain.entities import KeyResult

from user.models import UserORM
from team.models import TeamORM
from objective.models import ObjectiveORM
from key_result.models import KeyResultORM


def map_key_result_orm_to_entity(kr_orm: KeyResultORM) -> KeyResult:
    """Converte um KeyResultORM (modelo Django) para uma entidade KeyResult."""
    return KeyResult(
        id=str(kr_orm.id),
        type=kr_orm.type,
        mode=kr_orm.mode,
        title=kr_orm.title,
        owner=str(kr_orm.owner.id),
        format=kr_orm.format,
        objectiveId=str(kr_orm.objective.id),
        comment_count=kr_orm.comment_count,
        goal=kr_orm.goal,
        initial_value=kr_orm.initial_value,
        team=str(kr_orm.team) if kr_orm.team else None,
        description=kr_orm.description,
        last_updated_by=kr_orm.last_updated_by,
        support_team=[str(i.id) for i in kr_orm.support_team.all()],
        created_at=kr_orm.created_at,
        updated_at=kr_orm.updated_at,
        deleted_at=kr_orm.deleted_at,
    )
    


def map_key_result_entity_to_orm(kr_entity: KeyResult) -> KeyResultORM:
    """Converte uma entidade KeyResult de domínio para um KeyResultORM (modelo Django)."""
    if kr_entity.id:
        try:
            kr_orm = KeyResultORM.objects.get(id=kr_entity.id)
        except KeyResultORM.DoesNotExist:
            raise ValueError(f"UserORM with ID {kr_entity.id} not found for update.") from None
    else:
        kr_orm = KeyResultORM()

    kr_orm.type=kr_entity.type
    kr_orm.mode=kr_entity.mode
    kr_orm.title=kr_entity.title
    kr_orm.format=kr_entity.format
    kr_orm.comment_count=kr_entity.comment_count
    kr_orm.goal=kr_entity.goal
    kr_orm.initial_value=kr_entity.initial_value
    kr_orm.description=kr_entity.description
    kr_orm.last_updated_by=kr_entity.last_updated_by
    
    if kr_entity.owner:
        try: 
            kr_orm.owner=UserORM.objects.get(id=kr_entity.owner)
        except UserORM.DoesNotExist:
            raise ValueError("Invalid User") from None
    
    if kr_entity.objective:
        try:
            kr_orm.objective=ObjectiveORM.objects.get(id=kr_entity.objective)
        except ObjectiveORM.DoesNotExist:
            raise ValueError("Invalid Objective") from None
        
    if kr_entity.team:
        try:
            kr_orm.team=TeamORM.objects.get(id=kr_entity.team)
        except TeamORM.DoesNotExist:
            raise ValueError("Invalid Team") from None
    
    if kr_entity.support_team:
        for i in kr_entity.support_team:
            try: 
                user=UserORM.objects.get(id=i)
                kr_orm.support_team.add(user)
            except UserORM.DoesNotExist:
                raise ValueError("Invalid User") from None
    
    return kr_orm
