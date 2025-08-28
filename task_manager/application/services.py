from typing import Optional, List

from task_manager.domain.entities import Task
from task_manager.application.interfaces import ITaskApplicationService, ITaskRepository
from task_manager.infrastructure.db.repositories import DjangoTaskRepository


class TaskApplicationService(ITaskApplicationService):
    def __init__(self, task_repository: ITaskRepository = None):
        self.task_repository = task_repository or DjangoTaskRepository()
    
    def get_tasks_by_filters(self, filter) -> Optional[List[Task]]:
        return self.task_repository.find_tasks_and_filter(filter)