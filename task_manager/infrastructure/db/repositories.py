from task_manager.application.interfaces import ITaskRepository

from cycle.models import CycleORM
from task_manager.application.interfaces import ITaskCommentRepository
from task_manager.infrastructure.db.mappers.task_comments_entity_to_orm import map_task_comments_entity_to_orm
from task_manager.infrastructure.db.mappers.task_comments_orm_to_entity import map_task_comments_orm_to_entity
from task_manager.models import TaskCommentsORM, TaskORM
from team.models import TeamCompany

from task_manager.infrastructure.api.v1.filters import TasksFilterSchema

from task_manager.infrastructure.db.mappers.task_orm_to_task_board_entity import map_task_orm_to_task_board_entity
from task_manager.infrastructure.db.mappers.task_orm_to_entity import map_task_orm_to_entity
from task_manager.infrastructure.db.mappers.task_entity_to_orm import map_task_entity_to_orm


class DjangoTaskRepository(ITaskRepository):
    def find_tasks_and_filter(self, filter: TasksFilterSchema):
        try:
            task_orm = TaskORM.objects.all()
            task_orm = filter.filter(task_orm)
            if filter.cy is None and filter.team_id:
                team = TeamCompany.objects.get(team_id=filter.team_id)
                cycles = CycleORM.objects.filter(team_id=team.company.id, active=True)
                task_orm = task_orm.filter(cycle__id__in=[cycle.id for cycle in cycles])
            return [map_task_orm_to_task_board_entity(i) for i in task_orm], 200, None 
        except TaskORM.DoesNotExist:
            return None, 404, {'error':'Task not exist.'}
        
    def find_task_by_id(self, id):
        try: 
            task_orm = TaskORM.objects.get(id=id)
            return map_task_orm_to_entity(task_orm), 200, None
        except TaskORM.DoesNotExist:
            return None, 404, {'error':'Task not exist.'}
        
    def create_task(self, payload):
        try:
            task_orm = map_task_entity_to_orm(payload)
            return map_task_orm_to_entity(task_orm), 200, None
        except:
            return None, 404, {'error':'Invalid Task'}
        
    def delete_task(self, id, user):
        try: 
            task_orm = TaskORM.objects.get(id=id)
            if task_orm.deleted_at:
                return 404, {'error':'Task already deleted.'}
            task_orm.delete_task(user=user)
            return 200, None
        except TaskORM.DoesNotExist:
            return 404, {'error':'Task not exist.'}
        
    def patch_task(self, id, data):
        try:
            task_orm = TaskORM.objects.get(id=id)
        except TaskORM.DoesNotExist:
            return None, 404, {'error': 'Task not exist.'}

        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(task_orm, key, value)

        task_orm.save()
        return map_task_orm_to_entity(task_orm), 200, None


class DjangoTaskCommentsRepository(ITaskCommentRepository):
    def find_comments_by_task_id(self, id):
        try: 
            comment_orm = TaskCommentsORM.objects.filter(task_id=id)
            return [map_task_comments_orm_to_entity(task_orm=i) for i in comment_orm], 200, None
        except TaskCommentsORM.DoesNotExist:
            return None, 404, {'error':'Task not exist.'}
        
    def create_task_comment(self, payload):
        try:
            comment_orm = map_task_comments_entity_to_orm(payload)
            return map_task_comments_orm_to_entity(comment_orm), 200, None
        except:
            return None, 404, {'error':'Invalid Comment'}
        
    def delete_task_comments_by_id(self, id):
        try: 
            comment_orm = TaskCommentsORM.objects.get(id=id)
            if comment_orm.deleted_at:
                return 404, {'error':'Task already deleted.'}
            comment_orm.soft_delete()
            return 200, None
        except TaskCommentsORM.DoesNotExist:
            return 404, {'error':'Task not exist.'}