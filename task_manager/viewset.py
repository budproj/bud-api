from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.response import Response

from task_manager.models import Task
from task_manager.serializers.task_serializer import TaskSerializer, TaskReadSerializer

from api.utils.translate_datetime import TranslateRelativeDate

class TaskViewset(viewsets.ViewSet):
    serializer_class = TaskSerializer

    def list(self, request, team_id=None):
        if not team_id:
            return Response('Team ID is required.', status=status.HTTP_400_BAD_REQUEST)

        tasks = Task.objects.all()
        filter = Q()

        # filter by team - required
        filter &= Q(team_id__id=team_id)

        # filter by KR
        key_result_id = request.query_params.get('kr')
        if key_result_id is not None and key_result_id != '':
            filter &= Q(key_result_id__id=key_result_id)

        # filter by cycle
        cycle = request.query_params.get('cycle')
        if cycle is not None and cycle != '':
            filter &= Q(cycle__cadence=cycle)

        # filter by date
        last = request.query_params.get('last')
        since = request.query_params.get('since')
        upto = request.query_params.get('upto')
        
        date_range = TranslateRelativeDate(
            timezone, last=last, since=since, upto=upto
        ).date_range
    
        if date_range:
            filter &= Q(created_at__range=date_range)
        
        filter &= Q(deleted_at__isnull=True)
            
        tasks = tasks.filter(filter)
        serializer = TaskReadSerializer(tasks, many=True)
        return Response(serializer.data)

    def create(self, request, team_id=None):
        data = request.data.copy()
        serializer = TaskSerializer(data=data, context={'team_id', team_id})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_one(self, request, team_id, pk):
        task = get_object_or_404(Task.objects.prefetch_related('history'), id=pk)
        serializer = TaskReadSerializer(task, context={'team_id', team_id})
        return Response(serializer.data)
    
    
    def delete(self, request, team_id, task_id):
        task = get_object_or_404(Task, id=task_id)

        if task.deleted_at:
            return Response(
                {'detail': 'A tarefa já foi deletada.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = request.user if request.user.is_authenticated else None

        task.delete_task(user=user)

        serializer = TaskSerializer(task, context={'team_id', team_id})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, task_id=None, team_id=None):
        try:
            task = get_object_or_404(Task, id=task_id)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=404)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
      