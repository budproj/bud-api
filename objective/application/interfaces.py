from abc import ABC, abstractmethod
from typing import List, Optional

from objective.domain.entities import Objective


class IObjectiveService(ABC):
    @abstractmethod
    def patch_objective(self, objective_id: str, data: Objective) -> Optional[Objective]:
        pass
    
    @abstractmethod
    def list_objective_by_team_id(self, team_id: str) -> Optional[List[Objective]]:
        pass


class IObjectiveRepository(ABC):
    @abstractmethod
    def patch_objective(self, objective_id: str, data: Objective) -> Optional[Objective]:
        pass
    
    @abstractmethod
    def select_objective_by_team_id(self, team_id: str) -> Optional[List[Objective]]:
        pass
