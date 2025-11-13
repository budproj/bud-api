from task_manager.domain.entities.task_board import TaskBoard

from task_manager.models import TaskORM, TaskHistoryORM
from user.models import UserORM

from task_manager.infrastructure.db.mappers.task_history_orm_to_entity import map_task_history_orm_to_entity
from user.infrastructure.db.mappers import map_user_orm_to_entity
from key_result.infrastructure.db.mappers import map_key_result_orm_to_entity

def map_task_orm_to_task_board_entity(task_orm: TaskORM) -> TaskBoard:
    support_team_orm = UserORM.objects.filter(id__in=task_orm.support_team) if task_orm.support_team else None
    return TaskBoard(
        team=str(task_orm.team.id) if task_orm.team else None,
        keyResult=map_key_result_orm_to_entity(task_orm.key_result) if task_orm.key_result else None,
        cycle=str(task_orm.cycle.id) if task_orm.cycle else None,
        owner=str(task_orm.owner.id) if task_orm.owner else None,
        status=task_orm.status,
        title=task_orm.title,
        description=task_orm.description,
        priority=task_orm.priority,
        initialDate=task_orm.initial_date,
        dueDate=task_orm.due_date,
        supportTeam=[map_user_orm_to_entity(i) for i in support_team_orm] if support_team_orm else [],
        attachments=[i for i in task_orm.attachments] if task_orm.attachments else None,
        tags=[i for i in task_orm.tags] if task_orm.tags else None,
        orderindex=task_orm.orderindex,
        id=str(task_orm.id),
        createdAt=task_orm.created_at,
        updatedAt=task_orm.updated_at,
        deletedAt=task_orm.deleted_at,
        history=[map_task_history_orm_to_entity(i) for i in TaskHistoryORM.objects.filter(task_id=str(task_orm.id))],
        usersRelated=[map_user_orm_to_entity(task_orm.owner)]+[map_user_orm_to_entity(UserORM.objects.get(id=i)) for i in task_orm.support_team] if task_orm.support_team else [map_user_orm_to_entity(task_orm.owner)],
        ownerFullName=f'{task_orm.owner.first_name} {task_orm.owner.last_name}',
    )