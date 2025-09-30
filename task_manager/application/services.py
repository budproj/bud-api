from task_manager.application.interfaces import ITaskApplicationService, ITaskRepository
from task_manager.infrastructure.db.repositories import DjangoTaskRepository


class TaskApplicationService(ITaskApplicationService):
    def __init__(self, task_repository: ITaskRepository = None):
        self.task_repository = task_repository or DjangoTaskRepository()
    
    def get_tasks_by_filters(self, filter):
        if filter.team_id or filter.key_result_id:
            return self.task_repository.find_tasks_and_filter(filter)
        return None, 404, {'error': 'Input Error: Team or Key Result id is needed.'}
    
    def get_task_by_id(self, id):
        return self.task_repository.find_task_by_id(id)
    
    def create_task(self, payload):
        return self.task_repository.create_task(payload)
    
    def delete_task(self, id, user):
        return self.task_repository.delete_task(id, user)
    
    def patch_task(self, id, data):
        return self.task_repository.patch_task(id, data)