from typing import List
from ninja import Router

from objective.application.interfaces import IObjectiveService
from objective.application.services import ObjectiveApplicationService

from objective.domain.entities import Objective

objective_router = Router(tags=["objective"])

objective_service: IObjectiveService = ObjectiveApplicationService()

@objective_router.get("team/{team_id}", response={200: List[Objective], 404: dict})
def list_objective_by_team(request, team_id: str):
    objective = objective_service.list_objective_by_team_id(team_id)
    return objective

@objective_router.patch("/{objective_id}", response={200: Objective, 404: dict})
def patch_objective(request, objective_id: str, data: Objective):
    objective = objective_service.patch_objective(objective_id, data)
    return objective