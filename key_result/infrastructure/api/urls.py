from django.urls import path
from ninja import NinjaAPI

from api.application.auth_guardian import AuthPermission
from key_result.infrastructure.api.v1.endpoints import kr_router

api = NinjaAPI(version="1.0.0", urls_namespace='key_result', title="Key Result", auth=AuthPermission())

api.add_router("/key-result", kr_router)

urlpatterns = [
    path("", api.urls),
]