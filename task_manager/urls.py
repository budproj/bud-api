from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from task_manager.viewset import TaskViewset

router = DefaultRouter(trailing_slash=True)
router.register(r'task', TaskViewset, basename="task")

task_list = TaskViewset.as_view({
    'get': 'list',
    'post': 'create'
})

task_detail = TaskViewset.as_view({
    'get': 'get_one',
    'put': 'update',
    'delete': 'delete'
})

urlpatterns = format_suffix_patterns([
    path('task/', task_list, name='task-list'),
    path('task/<uuid:task_id>', task_detail, name='task-detail'),
])
