from rest_framework import viewsets, status
from rest_framework.response import Response

from task_manager.serializers.task_comments_serializer import TaskCommentsSerializer
from task_manager.models import TaskComments

class TaskCommentsViewset(viewsets.ViewSet):
    serializer_class = TaskCommentsSerializer
    queryset = TaskComments.objects.all()

    def list(self, request, id):
        if id is None or id == '':
            return Response('O id da tarefa é obrigatório', status=status.HTTP_400_BAD_REQUEST)

        queryset = self.queryset.filter(task__id = id, deleted_at__isnull=True)
        serializer = self.serializer_class(queryset.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response('Bad request', status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        queryset = self.queryset.get(id=id)
        if queryset.deleted_at:
            return Response(
                {'detail': 'A tarefa já foi deletada.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
            
        queryset.soft_delete()
        serializer = self.serializer_class(queryset)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        