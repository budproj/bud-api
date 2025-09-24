from abc import ABC, abstractmethod
from typing import Optional, List, Tuple, Dict

from task_manager.domain.entities import Task, TaskBoard, TaskComments, TaskPatch
from task_manager.infrastructure.api.v1.filters import TasksFilterSchema
from user.models import UserORM

class ITaskApplicationService(ABC):
    @abstractmethod
    def get_tasks_by_filters(self, filter: TasksFilterSchema) -> Tuple[Optional[List[TaskBoard]], int, Optional[Dict[str,str]]]:
        pass
    
    @abstractmethod
    def get_task_by_id(self, id: str) -> Tuple[Optional[Task], int, Optional[Dict[str,str]]]:
        pass
    
    @abstractmethod
    def create_task(self, payload: Task) -> Tuple[Optional[Task], int, Optional[Dict[str,str]]]:
        pass
    
    @abstractmethod
    def delete_task(self, id: str, user: UserORM) -> Tuple[int, Optional[Dict[str,str]]]:
        pass
    
    @abstractmethod
    def patch_task(self, id: str, data: TaskPatch) -> Tuple[Optional[Task], int, Optional[Dict[str,str]]]:
        pass


class ITaskRepository(ABC):
    @abstractmethod
    def find_tasks_and_filter(self, filter) -> Tuple[Optional[List[TaskBoard]], int, Optional[Dict[str,str]]]:
        pass
    
    @abstractmethod
    def find_task_by_id(self, id: str) -> Tuple[Optional[Task], int, Optional[Dict[str,str]]]:
        pass
    
    @abstractmethod
    def create_task(self, payload: Task) -> Tuple[Optional[Task], int, Optional[Dict[str,str]]]:
        pass
    
    @abstractmethod
    def delete_task(self, id: str, user: UserORM) -> Tuple[int, Optional[Dict[str,str]]]:
        pass
    
    @abstractmethod
    def patch_task(self, id: str, data: TaskPatch) -> Tuple[Optional[Task], int, Optional[Dict[str,str]]]:
        pass

class ITaskCommentApplicationService(ABC):
    @abstractmethod
    def get_tasks_by_filters(self, filter) -> Optional[List[TaskComments]]:
        pass


class ITaskCommentRepository(ABC):
    @abstractmethod
    def find_tasks_and_filter(self, filter) -> Optional[List[TaskComments]]:
        pass