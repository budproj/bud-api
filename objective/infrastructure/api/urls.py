from django.urls import path
from ninja import NinjaAPI

from api.application.auth_guardian import AuthPermission
from objective.infrastructure.api.v1.endpoints import objective_router

api = NinjaAPI(version="1.0.0", urls_namespace='objective', title="Objective", auth=AuthPermission())

api.add_router("/objective", objective_router)

urlpatterns = [
    path("", api.urls),
]