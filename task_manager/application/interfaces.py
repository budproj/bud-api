from abc import ABC, abstractmethod
from typing import Optional, List

from task_manager.domain.entities import Task


class ITaskApplicationService(ABC):
    @abstractmethod
    def get_tasks_by_filters(self, filter) -> Optional[List[Task]]:
        pass


class ITaskRepository(ABC):
    @abstractmethod
    def find_tasks_and_filter(self, filter) -> Optional[List[Task]]:
        pass
