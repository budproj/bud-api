from task_manager.domain.entities.task_board import TaskHistory
from task_manager.models import TaskHistoryORM

def map_task_history_orm_to_entity(task_history_orm: TaskHistoryORM) -> TaskHistory:
    return TaskHistory(
        task=str(task_history_orm.task.id),
        field=task_history_orm.field,
        old_state=task_history_orm.old_state,
        new_state=task_history_orm.new_state,
        author=str(task_history_orm.author.id),
    )