from django.urls import path, include
from rest_framework.routers import DefaultRouter
from task_manager.viewset import TaskViewset

router = DefaultRouter()
router.register(r'task', TaskViewset, basename="task")

urlpatterns = [
    path('<team_id>/', include(router.urls)),
]
