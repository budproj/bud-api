from ninja import Router, Query
from typing import List

from task_manager.domain.entities import Task
from task_manager.infrastructure.api.v1.filters import TasksFilterSchema
from task_manager.application.interfaces import ITaskApplicationService
from task_manager.application.services import TaskApplicationService

task_router = Router(tags=["task_manager"])

task_service: ITaskApplicationService = TaskApplicationService()

@task_router.get("/task", response={200: List[Task], 404: dict})
def get_tasks_and_filter(request, filters: TasksFilterSchema = Query(...)):
    data = task_service.get_tasks_by_filters(filter.get_filter_expression())
    return data