from django.urls import path
from task_manager.viewset import TaskViewset

urlpatterns = [
    path('task/list', TaskViewset.as_view({"get": "list"})),
    path('task/get/<uuid:task_id>', TaskViewset.as_view({"get": "get_one"})),
    path('task/delete/<uuid:task_id>', TaskViewset.as_view({"delete": "delete"})),
    path('task/update/<uuid:task_id>', TaskViewset.as_view({"put": "update"})),
    path('task/create', TaskViewset.as_view({"post": "create"}))
]
