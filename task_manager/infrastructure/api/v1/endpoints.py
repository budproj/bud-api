from ninja import Router, Query
from typing import List

from task_manager.domain.entities import Task, TaskBoard, TaskPatch
from task_manager.infrastructure.api.v1.filters import TasksFilterSchema
from task_manager.application.interfaces import ITaskApplicationService
from task_manager.application.services import TaskApplicationService

task_router = Router(tags=["task_manager"])

task_service: ITaskApplicationService = TaskApplicationService()

@task_router.get("/task", response={200: List[TaskBoard], 404: dict})
def get_tasks_and_filter(request, filters: TasksFilterSchema = Query(...)):
    data, status_code, error = task_service.get_tasks_by_filters(filters)
    if error:
        return status_code, error
    return status_code, data

@task_router.get("/task/{id}", response={200: Task, 404: dict})
def get_task_by_id(request, id: str):
    data, status_code, error = task_service.get_task_by_id(id)
    if error:
        return status_code, error
    return status_code, data


@task_router.post("/task", response={200: Task, 404: dict})
def create_task(request, payload: Task):
    data, status_code, error = task_service.create_task(payload)
    if error:
        return status_code, error
    return status_code, data

@task_router.delete("/task/{id}", response={200: dict, 404: dict})
def delete_task(request, id: str):
    status_code, error = task_service.delete_task(id, request.auth)
    if error:
        return status_code, error
    return status_code, {'message': 'Task deleted successfully'}

@task_router.patch("/task/{id}", response={200: Task, 404: dict})
def patch_task(request, id: str, data: TaskPatch):
    task, status_code, error = task_service.patch_task(id, data)
    if error:
        return status_code, error
    return status_code, task