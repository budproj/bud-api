from typing import Any

from django.db import IntegrityError
from django.core.exceptions import ValidationError
from cycle.models import CycleORM
from key_result.models import KeyResultORM
from task_manager.domain.entities import TaskBoard, TaskComments, Task, TaskHistory

from task_manager.models import TaskCommentsORM, TaskORM, TaskHistoryORM
from team.models import TeamORM
from user.models import UserORM

from user.infrastructure.db.mappers import map_user_orm_to_entity
from key_result.infrastructure.db.mappers import map_key_result_orm_to_entity

def add_to_model(value: Any, model):
    if value:
        try: 
            return model.objects.get(id=value)
        except model.DoesNotExist:
            return None
    return None

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

def map_task_history_orm_to_entity(task_history_orm: TaskHistoryORM) -> TaskHistory:
    return TaskHistory(
        task=str(task_history_orm.task.id),
        field=task_history_orm.field,
        old_state=task_history_orm.old_state,
        new_state=task_history_orm.new_state,
        author=str(task_history_orm.author.id),
    )

def map_task_orm_to_task_board_entity(task_orm: TaskORM) -> TaskBoard:
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
        supportTeam=[i for i in task_orm.support_team] if task_orm.support_team else [],
        attachments=[i for i in task_orm.attachments] if task_orm.attachments else None,
        tags=[i for i in task_orm.tags] if task_orm.tags else None,
        orderindex=task_orm.orderindex,
        id=str(task_orm.id),
        createdAt=task_orm.created_at,
        updatedAt=task_orm.updated_at,
        deletedAt=task_orm.deleted_at,
        history=[map_task_history_orm_to_entity(i) for i in TaskHistoryORM.objects.filter(task_id=str(task_orm.id))],
        usersRelated=[map_user_orm_to_entity(task_orm.owner)]+[map_user_orm_to_entity(UserORM.objects.get(i)) for i in task_orm.support_team] if task_orm.support_team else [map_user_orm_to_entity(task_orm.owner)],
        ownerFullName=f'{task_orm.owner.first_name} {task_orm.owner.last_name}',
    )
    
def map_task_entity_to_orm(tk_entity: Task) -> TaskORM:
    if tk_entity.id:
        try:
            tk_orm = TaskORM.objects.get(id=tk_entity.id)
        except TaskORM.DoesNotExist:
            raise ValueError(f"TaskORM with ID {tk_entity.id} not found for update.") from None
    else:
        tk_orm = TaskORM()

    tk_orm.status = tk_entity.status
    tk_orm.title = tk_entity.title
    tk_orm.description = tk_entity.description
    tk_orm.priority = tk_entity.priority
    tk_orm.initial_date = tk_entity.initialDate
    tk_orm.due_date = tk_entity.dueDate
    tk_orm.support_team = [user for user in tk_entity.supportTeam] if tk_entity.supportTeam else []
    tk_orm.attachments = [att for att in tk_entity.attachments] if tk_entity.attachments else []
    tk_orm.tags = [tags for tags in tk_entity.tags] if tk_entity.tags else []
    tk_orm.orderindex = tk_entity.orderindex
    tk_orm.team = add_to_model(tk_entity.team, TeamORM)
    tk_orm.key_result = add_to_model(tk_entity.keyResult, KeyResultORM)
    tk_orm.cycle = add_to_model(tk_entity.cycle, CycleORM)
    tk_orm.owner = add_to_model(tk_entity.owner, UserORM)
    
    tk_orm.full_clean()
    tk_orm.save()
    
    return tk_orm
    
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