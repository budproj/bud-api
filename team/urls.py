from django.urls import path, include

app_name = "team"

urlpatterns = [
    path("api/", include("team.infrastructure.api.urls")),
]