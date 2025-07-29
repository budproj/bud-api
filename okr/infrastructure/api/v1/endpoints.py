from typing import List
from ninja import Router

from okr.application.interfaces import IKeyResultApplicationService, ICycleApplicationService
from okr.application.services import KeyResultApplicationService, CycleApplicationService
from okr.domain.entities import Cycle, CycleDate
from okr.infrastructure.api.v1.schemas import KeyResultOut

okr_router = Router(tags=["Users"])

kr_service: IKeyResultApplicationService = KeyResultApplicationService()
cycle_service: ICycleApplicationService = CycleApplicationService()

@okr_router.get("/key_result/{team_id}", response={200: List[KeyResultOut], 404: dict})
def get_kr_by_team(request, team_id: str):
    data = kr_service.get_key_results_by_team_id(team_id)
    return data

@okr_router.get("/cycle/{team_id}", response={200: List[Cycle], 404: dict})
def get_cycle_by_team(request, team_id: str):
    data = cycle_service.get_cycle_by_team_id(team_id)
    return data
  
@okr_router.get("/cycle/date/{team_id}", response={200: List[CycleDate], 404: dict})
def get_cycle_dates_by_team(request, team_id: str):
    data = cycle_service.get_cycle_date_by_team_id(team_id)
    return data