from django.urls import path, include

app_name = "objective"

urlpatterns = [
    path("api/", include("objective.infrastructure.api.urls")),
]