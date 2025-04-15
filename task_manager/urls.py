from django.urls import path
from task_manager.viewset import TaskViewset

urlpatterns = [
    path('task', TaskViewset.as_view({"get": "list", "post": "create"})),
    path('task/<uuid:id>', TaskViewset.as_view({"get": "get_one", "delete": "delete", "put": "update"})),
]
