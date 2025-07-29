from django.urls import path, include

app_name = "okr"

urlpatterns = [
    path("api/", include("okr.infrastructure.api.urls")),
]