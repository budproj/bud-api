from abc import ABC, abstractmethod
from typing import List, Optional

from okr.domain.entities import Cycle, CycleDate, KeyResult


class IKeyResultApplicationService(ABC):
    @abstractmethod
    def get_key_results_by_team_id(self, team_id) -> Optional[List[KeyResult]]:
        pass


class IKeyResultRepository(ABC):
    @abstractmethod
    def find_by_team_id(self, team_id) -> Optional[List[KeyResult]]:
        pass


class ICycleApplicationService(ABC):
    @abstractmethod
    def get_cycle_by_team_id(self, team_id) -> Optional[List[Cycle]]:
        pass
    
    @abstractmethod
    def get_cycle_date_by_team_id(self, team_id) -> Optional[List[CycleDate]]:
        pass


class ICycleRepository(ABC):
    @abstractmethod
    def find_cycle_by_team_id(self, team_id) -> Optional[List[Cycle]]:
        pass
    
    @abstractmethod
    def find_cycle_dates_by_team_id(self, team_id) -> Optional[List[CycleDate]]:
        pass


class ITeamRepository(ABC):
    @abstractmethod
    def find_team_company_by_id(self, team_id) -> Optional[str]:
        pass