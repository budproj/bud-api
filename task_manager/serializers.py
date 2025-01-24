from rest_framework.serializers import ModelSerializer
from task_manager.models import Task, TaskHistory

class TaskHistorySerializer(ModelSerializer):
    class Meta:
        model = TaskHistory
        fields = '__all__'

class TaskSerializer(ModelSerializer):
    history = TaskHistorySerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = '__all__'
        read_only = ['team_id', 'created_at', 'update_at', 'deleted_at']