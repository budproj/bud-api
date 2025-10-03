from key_result.application.interfaces import IKeyResultApplicationService, IKeyResultRepository
from key_result.infrastructure.db.repositories import DjangoKeyResultRepository


class KeyResultApplicationService(IKeyResultApplicationService):
    def __init__(self, kr_repository: IKeyResultRepository = None):
        self.kr_repository = kr_repository or DjangoKeyResultRepository()
    
    def get_key_results_by_team_id(self, team_id, filters):
        return self.kr_repository.find_by_team_id(team_id, filters)
    
    def get_key_results_by_user_id(self, user_id):
        return self.kr_repository.find_by_user_id(user_id)
    
    def get_key_results_and_tasks_by_user_id(self, user_id):
        return self.kr_repository.find_kr_and_tasks_by_user_id(user_id)
    
    def patch(self, key_result_id, data):
        return self.kr_repository.update_key_result(key_result_id, data)
    
    def get_one(self, key_result_id):
        return self.kr_repository.get_one(key_result_id)
