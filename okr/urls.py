from django.urls import path
from okr.viewsets.key_result_viewset import KeyResultViewset

urlpatterns = [
    path('kr/<uuid:team_id>/<objective_id>/', KeyResultViewset.as_view({'get': 'list'})),
    path('kr/owner/<uuid:owner>/<objective_id>/', KeyResultViewset.as_view({'get': 'list_by_user'})),
    path('kr/task/<uuid:pk>/', KeyResultViewset.as_view({'get': 'list_by_user_with_tasks'})),
]