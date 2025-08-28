from typing import Optional, List

from django.db.models import Q

from task_manager.models import TaskORM
from task_manager.domain.entities import Task
from task_manager.application.interfaces import ITaskRepository
from task_manager.infrastructure.db.mappers import map_task_orm_to_task_board_entity

class DjangoTaskRepository(ITaskRepository):
    def find_tasks_and_filter(self, filter: Q) -> Optional[List[Task]]:
        try:
            task_orm = TaskORM.objects.filter(filter)
            return [map_task_orm_to_task_board_entity(i) for i in task_orm]
        except TaskORM.DoesNotExist:
            return None