from rest_framework.serializers import ModelSerializer
from task_manager.models import TaskHistory

class TaskHistorySerializer(ModelSerializer):
    class Meta:
        model = TaskHistory
        fields = '__all__'