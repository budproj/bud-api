from django.urls import path
from ninja import NinjaAPI

from okr.infrastructure.api.v1.endpoints import okr_router

api = NinjaAPI(version="1.0.0", title="Users API")

api.add_router("/okr", okr_router)

urlpatterns = [
    path("", api.urls),
]