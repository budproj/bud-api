from task_manager.domain.entities.task import Task

from task_manager.models import TaskORM


def map_task_orm_to_entity(task_orm: TaskORM) -> Task:
    return Task(
        team=str(task_orm.team.id) if task_orm.team else None,
        keyResult=str(task_orm.key_result.id) if task_orm.key_result else None,
        cycle=str(task_orm.cycle.id) if task_orm.cycle else None,
        owner=str(task_orm.owner.id) if task_orm.owner else None,
        status=task_orm.status,
        title=task_orm.title,
        description=task_orm.description,
        priority=task_orm.priority,
        initialDate=task_orm.initial_date,
        dueDate=task_orm.due_date,
        supportTeam=[i for i in task_orm.support_team] if task_orm.support_team else None,
        attachments=[i for i in task_orm.attachments] if task_orm.attachments else None,
        tags=[i for i in task_orm.tags] if task_orm.tags else None,
        orderindex=task_orm.orderindex,
        id=str(task_orm.id),
        createdAt=task_orm.created_at,
        updatedAt=task_orm.updated_at,
        deletedAt=task_orm.deleted_at,
    )
