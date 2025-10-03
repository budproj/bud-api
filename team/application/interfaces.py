from abc import ABC, abstractmethod
from typing import List, Optional

from team.domain.entities import Team

class ITeamRepository(ABC):
    @abstractmethod
    def list_teams_by_company_id(self, company_id: str) -> Optional[List[Team]]:
        pass
    
    @abstractmethod
    def get_team_from_id(self, team_id: str) -> Optional[Team]:
        pass
    
    @abstractmethod
    def check_user_in_team(self, team_id: str, user_id: str) -> bool:
        pass
    
class ITeamApplicationService(ABC):
    @abstractmethod
    def get_team_by_company_id(self, company_id: str) -> Optional[List[Team]]:
        pass