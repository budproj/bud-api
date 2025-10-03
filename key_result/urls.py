from django.urls import path, include

app_name = "key_result"

urlpatterns = [
    path("api/", include("key_result.infrastructure.api.urls")),
]