from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from task_manager.models import Task, Team
from task_manager.serializers import TaskSerializer
from datetime import datetime

class TaskViewset(viewsets.ViewSet):

    def list(self, request, team_id=None):
        if not team_id:
            return Response("Team ID is required.", status=status.HTTP_400_BAD_REQUEST)
        
        tasks = Task.objects.filter(team_id=team_id)
        
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
        
       
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_one(self, request, team_id, task_id):
        task = get_object_or_404(Task.objects.prefetch_related('history'), id=task_id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
