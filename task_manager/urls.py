from django.urls import path
from task_manager.viewset import TaskViewset

urlpatterns = [
    path('<team_id>/task/', TaskViewset.as_view({'get': 'list'})),
    path('<team_id>/task/<task_id>', TaskViewset.as_view({'get': 'get_one'})),
    path('<team_id>/task/<uuid:task_id>', TaskViewset.as_view({'put': 'put'})),
    path('<team_id>/task/<uuid:task_id>', TaskViewset.as_view({'delete': 'delete_one'})),
    path('<team_id>/task/', TaskViewset.as_view({'post': 'create'})),
]
