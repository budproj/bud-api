from rest_framework.serializers import ModelSerializer
from task_manager.models import TaskHistoryORM
from user.serializers.user_serializer import UserSerializer

class TaskHistorySerializer(ModelSerializer):
    author = UserSerializer(read_only=True)
    
    class Meta:
        model = TaskHistoryORM
        fields = '__all__'