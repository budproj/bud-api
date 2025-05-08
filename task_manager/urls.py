from django.urls import path

from task_manager.viewsets.task_viewset import TaskViewset
from task_manager.viewsets.task_comments_viewset import TaskCommentsViewset

urlpatterns = [
    path('task', TaskViewset.as_view({'get': 'list', 'post': 'create'})),
    path('task/<uuid:id>', TaskViewset.as_view({'get': 'get_one', 'delete': 'delete', 'put': 'update'})),
    path('task/comments', TaskCommentsViewset.as_view({'post': 'create'})),
    path('task/comments/<uuid:id>', TaskCommentsViewset.as_view({'get': 'list', 'delete': 'delete'})),
]
