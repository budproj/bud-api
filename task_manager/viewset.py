from datetime import datetime

from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.utils.timezone import now
from rest_framework import viewsets, status
from rest_framework.response import Response

from task_manager.models import Task, Team
from task_manager.serializers import TaskSerializer
from datetime import datetime

class TaskViewset(viewsets.ViewSet):

    def list(self, request, team_id=None):
        if not team_id:
            return Response("Team ID is required.", status=status.HTTP_400_BAD_REQUEST)

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
        if last:
            time_relative, keyword = last.split(' ')
            now = timezone.now()
            if time_relative == '0':
                date_start, date_end = TranslateRelativeDate.current(now, keyword) 
                filter &= Q(created_at__range=(date_start, date_end))
            else:
                date_start, date_end = TranslateRelativeDate.last(now, keyword, time_relative)
                filter &= Q(created_at__range=(date_start, date_end))
            
        since = request.query_params.get('since')
        upto = request.query_params.get('upto')
        
        if since and upto:
            now = timezone.now()
            date_start, date_end = TranslateRelativeDate.between(now, since, upto)
            filter &= Q(created_at__range=(date_start, date_end))
        elif since:
            now = timezone.now()
            date_start, date_end = TranslateRelativeDate.since(now, since)
            filter &= Q(created_at__range=(date_start, date_end))
            
        tasks = tasks.filter(filter)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def post(self, request, team_id=None):
        
        #if not request.user.is_authenticated:
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
            return Response({"detail": "A tarefa já foi deletada."}, status=status.HTTP_400_BAD_REQUEST)

        user = request.user if request.user.is_authenticated else None

        task.delete_task(user=user)

        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    