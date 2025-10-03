from django.urls import path, include

app_name = "cycle"

urlpatterns = [
    path("api/", include("cycle.infrastructure.api.urls")),
]