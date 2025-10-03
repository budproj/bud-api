from ninja import Router, Query
from typing import List

from task_manager.application.interfaces import ITaskApplicationService, ITaskCommentApplicationService
from task_manager.application.services import TaskApplicationService, TaskCommentApplicationService

from task_manager.domain.entities.task import Task
from task_manager.domain.entities.task_board import TaskBoard
from task_manager.domain.entities.task_comments import TaskComments
from task_manager.domain.entities.task_patch import TaskPatch

from task_manager.infrastructure.api.v1.filters import TasksFilterSchema

task_router = Router(tags=["task_manager"])

task_service: ITaskApplicationService = TaskApplicationService()
task_comments_service: ITaskCommentApplicationService = TaskCommentApplicationService()

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

@task_router.get("/task/comments/task/{id}", response={200: TaskComments, 404: dict})
def get_task_comments_by_task_id(request, id: str):
    data, status_code, error = task_comments_service.get_task_comments_by_task_id(id)
    if error:
        return status_code, error
    return status_code, data

@task_router.post("/task/comments", response={200: TaskComments, 404: dict})
def create_task_comment(request, payload: TaskComments):
    data, status_code, error = task_comments_service.create_task_comment(payload)
    if error:
        return status_code, error
    return status_code, data

@task_router.delete("/task/comments/{id}", response={200: dict, 404: dict})
def delete_task_comment_by_id(request, id: str):
    status_code, error = task_comments_service.delete_task_comments_by_id(id)
    if error:
        return status_code, error
    return status_code, {'message': 'Task comment deleted successfully'}