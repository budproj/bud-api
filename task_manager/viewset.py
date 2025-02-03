from django.db.models import Q
from django.utils import timezone

from rest_framework import viewsets, status
from rest_framework.response import Response

from task_manager.models import Task
from task_manager.serializers import TaskSerializer

from api.utils.translate_datetime import TranslateRelativeDate


class TaskViewset(viewsets.ViewSet):
    def list(self, request, team_id=None):
        if not team_id:
            return Response('Team ID is required.', status=status.HTTP_400_BAD_REQUEST)

        tasks = Task.objects.all()
        filter = Q()

        # filter by team - required
        filter &= Q(team_id__id=team_id)

        # filter by KR
        key_result_id = request.query_params.get('kr')
        if key_result_id:
            filter &= Q(key_result_id__id=key_result_id)

        # filter by cycle
        cycle = request.query_params.get('cycle')
        if cycle:
            filter &= Q(key_result_id__objective__cycle=cycle)

        # filter by date
        last = request.query_params.get('last')
        since = request.query_params.get('since')
        upto = request.query_params.get('upto')
        date_range = TranslateRelativeDate(
            timezone, last=last, since=since, upto=upto
        ).date_range
        filter &= Q(created_at__range=date_range)

        tasks = tasks.filter(filter)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def create(self, request, team_id=None):
        serializer = TaskSerializer(
            data=request.data, context={'team_id', team_id})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer, status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
