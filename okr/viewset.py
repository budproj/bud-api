from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from okr.serializers.key_result_serializer import KeyResultSerializer
from okr.serializers.cycle_serializer import CycleSerializer
from okr.models import KeyResult, Cycle

class KeyResultViewset(ModelViewSet):

    def list(self, request, team_id=None, objective_id=None):
        queryset = KeyResult.objects.filter(deleted_at=None, team__id=team_id, objective__cycle__active=True)

        if objective_id not in [None, '0']:
            queryset = queryset.filter(objective__id=objective_id)

        serializer = KeyResultSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def list_by_user(self, request, owner=None, objective_id=None):
        queryset = KeyResult.objects.filter(deleted_at=None, owner=owner, objective__cycle__active=True, team__isnull=False)

        if objective_id not in [None, '0']:
            queryset = queryset.filter(objective__id=objective_id)

        serializer = KeyResultSerializer(queryset, many=True)
        return Response(serializer.data)

class CycleViewset(ModelViewSet):
    
    def list(self, request, team_id=None):
        queryset = Cycle.objects.filter(deleted_at=None, team__id=team_id)
        
        serializer = CycleSerializer(queryset, many=True)
        return Response(serializer.data)