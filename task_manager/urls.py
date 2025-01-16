from django.urls import path
from task_manager.viewset import TaskViewset

urlpatterns = [
    path('<team_id>/task/', TaskViewset.as_view({"get": "list"})),
    path('<team_id>/task/', TaskViewset.as_view({"post": "create"}))
]