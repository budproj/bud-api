from django.urls import path
from ninja import NinjaAPI

from api.application.auth_guardian import AuthPermission
from team.infrastructure.api.v1.endpoints import team_router

api = NinjaAPI(version="1.0.0", urls_namespace='team', title="Team", auth=AuthPermission())

api.add_router("/team", team_router)

urlpatterns = [
    path("", api.urls),
]