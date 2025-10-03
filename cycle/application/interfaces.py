from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Tuple

from cycle.domain.entities import Cycle, CycleDate


class ICycleApplicationService(ABC):
    @abstractmethod
    def get_cycle_by_team_id(self, team_id) -> Tuple[Optional[List[Cycle]], Optional[int], Optional[Dict[str, str]]]:
        pass
    
    @abstractmethod
    def get_all_cycles_by_team_id(self, team_id) -> Tuple[Optional[List[Cycle]], Optional[int], Optional[Dict[str, str]]]:
        pass


class ICycleRepository(ABC):
    @abstractmethod
    def find_cycle_by_team_id(self, team_id) -> Tuple[Optional[List[Cycle]], Optional[int], Optional[Dict[str, str]]]:
        pass
    
    @abstractmethod
    def find_all_cycles_by_team_id(self, team_id) -> Tuple[Optional[List[Cycle]], Optional[int], Optional[Dict[str, str]]]:
        pass
