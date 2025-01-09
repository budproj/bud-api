from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView
from rest_framework.decorators import action
from rest_framework.response import Response
from task_manager.models import Task
from task_manager.serializers import TaskSerializer


class TaskViewset(viewsets.ViewSet):
    def list(self, request, team_id=None):
        if not team_id:
            return Response("Team ID is required.", status=status.HTTP_400_BAD_REQUEST)
        
        tasks = Task.objects.filter(team_id=team_id)
        
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def create(self, request, team_id=None):
        serializer = TaskSerializer(data=request.data)
        serializer.team_id = team_id
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer, status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    
