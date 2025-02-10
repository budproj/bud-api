from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.response import Response
from task_manager.models import Task, Team
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

    def post(self, request, team_id=None):
        # if not request.user.is_authenticated:
        #    return Response({'error': 'Authentication required.'}, status=status.HTTP_401_UNAUTHORIZED)

        team = get_object_or_404(Team, id=team_id)

        data = request.data.copy()
        serializer = TaskSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_one(self, request, team_id, task_id):
        task = get_object_or_404(Task.objects.prefetch_related('history'), id=task_id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, team_id, task_id):
        task = get_object_or_404(Task, id=task_id)

        if task.deleted_at:
            return Response(
                {'detail': 'A tarefa já foi deletada.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = request.user if request.user.is_authenticated else None

        task.delete_task(user=user)

        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
