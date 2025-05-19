from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils import timezone

from rest_framework import viewsets, status
from rest_framework.response import Response

from task_manager.serializers.task_serializer import TaskSerializer, TaskReadSerializer
from task_manager.models import Task

from api.utils.translate_datetime import TranslateRelativeDate
from api.utils.decorators.filter_queryset import query_filter_allowed

class TaskViewset(viewsets.ViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    @query_filter_allowed([
        'team_id__id',
        'key_result_id__id',
        'deleted_at__isnull',
        'tasks_user',
    ])
    def list(self, request):
        last = request.query_params.get('last')
        since = request.query_params.get('since')
        upto = request.query_params.get('upto')

        date_range = TranslateRelativeDate(
            timezone, last=last, since=since, upto=upto
        ).date_range

        if date_range:
            self.queryset = self.queryset.filter(Q(created_at__range=date_range))

        serializer = TaskReadSerializer(self.queryset.all(), many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @query_filter_allowed(['team_id__id'])
    def get_one(self, request, id):        
        serializer = TaskReadSerializer(self.queryset.get(id=id))
        return Response(serializer.data)

    def delete(self, request, id):
        task = get_object_or_404(Task, id=id)

        if task.deleted_at:
            return Response(
                {'detail': 'A tarefa já foi deletada.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = request.user if request.user.is_authenticated else None

        task.delete_task(user=user)

        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, id=None, team_id=None):
        try:
            task = get_object_or_404(Task, id=id)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=404)
        serializer = TaskSerializer(task, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)