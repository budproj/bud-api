from django.db.models import Q

from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from okr.models import KeyResult
from okr.enums.key_result_choices import KeyResultModeChoices
from okr.serializers.key_result_serializer import KeyResultSerializer
from okr.serializers.key_result_task_serializer import KeyResultTaskSerializer

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
    
    def list_by_user_with_tasks(self, request, pk):
        queryset = KeyResult.objects.filter(
            mode=KeyResultModeChoices.PUBLISHED,
            deleted_at__isnull=True,
            objective__cycle__active=True,
        )
        queryset = queryset.filter(
            Q(owner__id=pk) | 
            Q(support_team__in=[pk])
        )
        serializer = KeyResultTaskSerializer(queryset, many=True, context={'user_selected': pk})
        return Response(serializer.data, status=status.HTTP_200_OK)