from typing import List
from ninja import Router

from cycle.application.interfaces import ICycleApplicationService
from cycle.application.services import CycleApplicationService

from cycle.domain.entities import Cycle, CycleDate

cycle_router = Router(tags=["cycle"])

cycle_service: ICycleApplicationService = CycleApplicationService()

@cycle_router.get("/team/{team_id}", response={200: List[Cycle], 404: dict})
def get_cycle_by_team(request, team_id: str):
    data, status_code, error = cycle_service.get_cycle_by_team_id(team_id)
    if not error:
        return status_code, data
    return status_code, error
  
@cycle_router.get("/date/{team_id}", response={200: List[CycleDate], 404: dict})
def get_cycle_dates_by_team(request, team_id: str):
    data = cycle_service.get_cycle_date_by_team_id(team_id)
    return 200, data
