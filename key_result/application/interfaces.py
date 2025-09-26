from abc import ABC, abstractmethod
from typing import List, Optional

from key_result.domain.entities import KeyResult


class IKeyResultApplicationService(ABC):
    @abstractmethod
    def get_key_results_by_team_id(self, team_id, filters) -> Optional[List[KeyResult]]:
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
    def update_key_result(self, key_result_id: str, data: KeyResult) -> Optional[KeyResult]:
        pass

    @abstractmethod
    def get_one(self, key_result_id: str) -> Optional[KeyResult]:
        pass