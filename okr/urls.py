from django.urls import path
from okr.viewset import KeyResultViewset, CycleViewset

urlpatterns = [
    path('kr/<team_id>/<objective_id>/', KeyResultViewset.as_view({'get': 'list'})),
    path('kr/owner/<owner>/<objective_id>/', KeyResultViewset.as_view({'get': 'list_by_user'})),
    path('kr/<kr_id>/', KeyResultViewset.as_view({'get': 'list_one'})),
    path('cycle/<team_id>/', CycleViewset.as_view({'get': 'list'})),
]