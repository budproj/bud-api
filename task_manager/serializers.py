from rest_framework.serializers import ModelSerializer
from task_manager.models import Task

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only = ['team_id', 'created_at', 'update_at', 'is_deleted']