from objective.application.interfaces import IObjectiveRepository, IObjectiveService
from objective.infrastructure.db.repositories import DjangoObjectiveRepository


class ObjectiveApplicationService(IObjectiveService):
    def __init__(self, objective_repository: IObjectiveRepository = None):
        self.objective_repository = objective_repository or DjangoObjectiveRepository()

    def patch_objective(self, objective_id, data):
        return self.objective_repository.patch_objective(objective_id, data)

    def list_objective_by_team_id(self, team_id):
        return self.objective_repository.select_objective_by_team_id(team_id)