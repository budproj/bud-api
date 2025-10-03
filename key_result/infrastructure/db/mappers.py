from django.db.models import Q

from task_manager.models import TaskORM
from user.models import UserORM
from team.models import TeamORM
from objective.models import ObjectiveORM
from key_result.models import KeyResultORM

from key_result.domain.entities.key_result import KeyResult
from key_result.domain.entities.key_result_with_tasks import KeyResultWTasks
from task_manager.domain.entities.task_summary import TaskSummary


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
            kr_orm.objective=ObjectiveORM.objects.get(id=kr_entity.objectiveId)
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


def map_task_orm_to_entity_summary(task_orm: TaskORM) -> TaskSummary:
    return TaskSummary(
        id=str(task_orm.id),
        teamId=str(task_orm.team.id) if task_orm.team else None,
        owner=str(task_orm.owner.id) if task_orm.owner else None,
        ownerFullName=f'{task_orm.owner.first_name} {task_orm.owner.last_name}' if task_orm.owner else None,
        status=task_orm.status,
        title=task_orm.title,
        description=task_orm.description,
        priority=task_orm.priority,
        supportTeam=[i for i in task_orm.support_team] if task_orm.support_team else None,
    )


def map_key_result_with_tasks_orm_to_entity(kr_orm: KeyResultORM) -> KeyResultWTasks:
    """Converte um KeyResultORM (modelo Django) para uma entidade KeyResultWTasks."""
    tasks = TaskORM.objects.filter(
        (Q(support_team__contains=[str(kr_orm.owner.id)]) & Q(key_result__id=str(kr_orm.id)) & Q(deleted_at__isnull=True)) | 
        (Q(owner__id=str(kr_orm.owner.id))) & Q(key_result__id=str(kr_orm.id)) & Q(deleted_at__isnull=True)
    ).order_by('id')
    return KeyResultWTasks(
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
        krTasks=[map_task_orm_to_entity_summary(i) for i in tasks]
    )
