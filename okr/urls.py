from django.urls import path
from okr.viewset import KeyResultViewset, CycleViewset

urlpatterns = [
    path('kr/<team_id>/<objective_id>/', KeyResultViewset.as_view({'get': 'list'})),
    path('cycle/<team_id>/', CycleViewset.as_view({'get': 'list'})),
]