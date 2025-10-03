from django.urls import path
from ninja import NinjaAPI

from api.application.auth_guardian import AuthPermission
from cycle.infrastructure.api.v1.endpoints import cycle_router

api = NinjaAPI(version="1.0.0", urls_namespace='cycle', title="Cycle", auth=AuthPermission())

api.add_router("/cycle", cycle_router)

urlpatterns = [
    path("", api.urls),
]