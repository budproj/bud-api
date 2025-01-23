from datetime import datetime

from django.db.models import Q
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView
from rest_framework.decorators import action
from rest_framework.response import Response

from task_manager.models import Task
from task_manager.serializers import TaskSerializer

from api.utils.translate_datetime import TranslateRelativeDate

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

            if time_relative == '0':
                print(keyword)
                filter &= TranslateRelativeDate.current(keyword)
            else:
                filter &= TranslateRelativeDate.last(keyword, time_relative)
            
        since = request.query_params.get('since')
        upto = request.query_params.get('upto')
        
        if since and upto:
            filter &= TranslateRelativeDate.between(since, upto)
        elif since:
            filter &= TranslateRelativeDate.since(since)
        print(filter)
        tasks = tasks.filter(filter)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def create(self, request, team_id=None):
        serializer = TaskSerializer(data=request.data)
        serializer.team_id = team_id
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer, status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    
