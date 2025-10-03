
from task_manager.domain.entities.task_comments import TaskComments

from task_manager.models import TaskCommentsORM

def map_task_comments_orm_to_entity(task_orm: TaskCommentsORM) -> TaskComments:
    return TaskComments(
        userId=str(task_orm.user.id) if task_orm.user.id else None,
        taskId=str(task_orm.task.id) if task_orm.task.id else None,
        id=str(task_orm.id),
        text=task_orm.text,
        parentId=str(task_orm.parent.id) if task_orm.parent.id else None,
        createdAt=task_orm.created_at,
        updatedAt=task_orm.updated_at,
        deletedAt=task_orm.deleted_at,
    )
