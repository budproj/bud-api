from django.urls import path
from ninja import NinjaAPI

from api.application.auth_guardian import AuthPermission
from task_manager.infrastructure.api.v1.endpoints import task_router

api = NinjaAPI(version="1.0.0", urls_namespace='tasks', title="Tasks", auth=AuthPermission())

api.add_router("/task-manager", task_router)

urlpatterns = [
    path("", api.urls),
]