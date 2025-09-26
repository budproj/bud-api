from typing import List
from ninja import Query, Router

from key_result.application.interfaces import IKeyResultApplicationService
from key_result.application.services import KeyResultApplicationService

from key_result.domain.entities import KeyResult
from key_result.infrastructure.api.v1.filters import KeyResultFilterSchema

kr_router = Router(tags=["key_result"])

kr_service: IKeyResultApplicationService = KeyResultApplicationService()

@kr_router.get("/{key_result_id}", response={200: KeyResult, 404: dict})
def get_kr(request, key_result_id: str):
    data = kr_service.get_one(key_result_id)
    return data

@kr_router.get("/team/{team_id}", response={200: List[KeyResult], 404: dict})
def get_kr_by_team(request, team_id: str, filters: KeyResultFilterSchema = Query(...)):
    data = kr_service.get_key_results_by_team_id(team_id, filters)
    return data

@kr_router.patch("/{key_result_id}", response={200: KeyResult, 404: dict})
def patch_objective(request, key_result_id: str, data: KeyResult):
    key_result = kr_service.patch(key_result_id, data)
    return key_result