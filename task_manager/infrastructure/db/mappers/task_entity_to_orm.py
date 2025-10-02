from typing import Any

from cycle.models import CycleORM
from key_result.models import KeyResultORM
from task_manager.models import TaskORM
from team.models import TeamCompany, TeamORM
from user.models import UserORM

from task_manager.domain.entities.task import Task

def add_to_model(value: Any, model):
    if value:
        try: 
            return model.objects.get(id=value)
        except model.DoesNotExist:
            return None
    return None

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
    tk_orm.owner = add_to_model(tk_entity.owner, UserORM)
    
    if tk_entity.cycle is None and tk_entity.keyResult is not None:
        key_result = KeyResultORM.objects.get(id=tk_entity.keyResult)
        tk_orm.cycle = key_result.objective.cycle
    elif tk_entity.cycle is None and tk_entity.team is not None:
        team = TeamCompany.objects.get(team_id=tk_entity.team)
        cycle = CycleORM.objects.get(active=True, team_id=team.company.id, cadence=CycleORM.CycleCadenceChoices.YEARLY)
        tk_orm.cycle = cycle
    elif tk_entity.team is None:
        tk_orm.cycle = None
    else: 
        tk_orm.cycle = add_to_model(tk_entity.cycle, CycleORM)
    
    tk_orm.full_clean()
    tk_orm.save()
    
    return tk_orm