from django.urls import path, include
from rest_framework.routers import DefaultRouter
from task_manager.viewset import TaskViewset

urlpatterns = [
    path('<team_id>/task/list', TaskViewset.as_view({"get": "list"})),
    path('<team_id>/task/get/<int:pk>', TaskViewset.as_view({"get": "get_one"})),
    path('<team_id>/task/delete/<uuid:task_id>', TaskViewset.as_view({"put": "delete_task"})),
    path('<team_id>/task/update/<int:pk>', TaskViewset.as_view({"patch": "update"})),
    path('<team_id>/task/create', TaskViewset.as_view({"post": "create"}))
]
