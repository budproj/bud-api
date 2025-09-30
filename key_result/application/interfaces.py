from abc import ABC, abstractmethod
from typing import List, Optional

from key_result.domain.entities.key_result import KeyResult
from key_result.domain.entities.key_result_with_tasks import KeyResultWTasks


class IKeyResultApplicationService(ABC):
    @abstractmethod
    def get_key_results_by_team_id(self, team_id, filters) -> Optional[List[KeyResult]]:
        pass
    
    @abstractmethod
    def get_key_results_by_user_id(self, user_id) -> Optional[List[KeyResult]]:
        pass
    
    @abstractmethod
    def get_key_results_and_tasks_by_user_id(self, user_id) -> Optional[List[KeyResultWTasks]]:
        pass
    
    @abstractmethod
    def patch(self, key_result_id: str, data: KeyResult) -> Optional[KeyResult]:
        pass
    
    @abstractmethod
    def get_one(self, key_result_id: str) -> Optional[KeyResult]:
        pass


class IKeyResultRepository(ABC):
    @abstractmethod
    def find_by_team_id(self, team_id, filters) -> Optional[List[KeyResult]]:
        pass
    
    @abstractmethod
    def find_by_user_id(self, user_id) -> Optional[List[KeyResult]]:
        pass
    
    @abstractmethod
    def find_kr_and_tasks_by_user_id(self, user_id: str) -> Optional[List[KeyResultWTasks]]:
        pass
    
    @abstractmethod
    def update_key_result(self, key_result_id: str, data: KeyResult) -> Optional[KeyResult]:
        pass

    @abstractmethod
    def get_one(self, key_result_id: str) -> Optional[KeyResult]:
        pass