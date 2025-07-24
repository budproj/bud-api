from abc import ABC, abstractmethod
from typing import List, Optional

from okr.domain.entities import KeyResult


class IKeyResultApplicationService(ABC):
    @abstractmethod
    def get_key_results_by_team_id(self, team_id) -> Optional[List[KeyResult]]:
        pass


class IKeyResultRepository(ABC):
    @abstractmethod
    def find_by_team_id(self, team_id) -> Optional[List[KeyResult]]:
        pass