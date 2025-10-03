from task_manager.domain.entities.task_comments import TaskComments

from task_manager.models import TaskCommentsORM, TaskORM
from user.models import UserORM
    
def map_task_comments_entity_to_orm(tk_entity: TaskComments) -> TaskCommentsORM:
    """Converte uma entidade TaskComments de domínio para um TaskCommentsORM (modelo Django)."""
    if tk_entity.id:
        try:
            tk_orm = TaskCommentsORM.objects.get(id=tk_entity.id)
        except TaskCommentsORM.DoesNotExist:
            raise ValueError(f"TaskCommentsORM with ID {tk_entity.id} not found for update.") from None
    else:
        tk_orm = TaskCommentsORM()

    tk_orm.text=tk_entity.text
    
    if tk_entity.parent:
        try: 
            tk_orm.parent = TaskCommentsORM.objects.get(id=tk_entity.parent)
        except TaskCommentsORM.DoesNotExist:
            raise ValueError("Invalid Parent") from None
    
    if tk_entity.user:
        try:
            tk_orm.user = UserORM.objects.get(id=tk_entity.user)
        except UserORM.DoesNotExist:
            raise ValueError("Invalid User") from None
        
    if tk_entity.task:
        try:
            tk_orm.task = TaskORM.objects.get(id=tk_entity.task)
        except TaskORM.DoesNotExist:
            raise ValueError("Invalid Task") from None
    
    return tk_orm
