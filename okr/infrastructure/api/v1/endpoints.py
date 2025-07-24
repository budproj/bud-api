from django.conf import settings
from ninja import Router

from okr.application.interfaces import IKeyResultApplicationService
from okr.application.services import KeyResultApplicationService
from okr.infrastructure.api.v1.schemas import KeyResultOut

okr_router = Router(tags=["Users"])

okr_service: IKeyResultApplicationService = KeyResultApplicationService()

@okr_router.get("/{team_id}", response={200: KeyResultOut, 404: dict})
def get_kr_by_team(request, team_id: str):
    return okr_service.get_key_results_by_team_id(team_id)
    