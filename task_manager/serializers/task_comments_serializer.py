from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from task_manager.models import TaskORM, TaskCommentsORM
from task_manager.serializers.task_serializer import TaskSerializer
from user.models import UserORM

class TaskCommentsSerializer(ModelSerializer):
    task = TaskSerializer(read_only=True)
    user = SerializerMethodField(read_only=True)
    
    class Meta:
        model = TaskCommentsORM
        fields = '__all__'
        
    def get_user(self, obj):
        return {
            'id': obj.user.id,
            'first_name': obj.user.first_name,
            'last_name': obj.user.last_name,
            'full_name': f'{obj.user.first_name} {obj.user.last_name}',
            'email': obj.user.email,
            'authz_sub': obj.user.authz_sub,
            'gender': obj.user.gender,
            'role': obj.user.role,
            'picture': obj.user.picture,
            'created_at': obj.user.created_at,
            'updated_at': obj.user.updated_at,
        }
        
    def create(self, validated_data):
        task_id = self.initial_data.get('task_id')
        user_id = self.initial_data.get('user_id')
        text = validated_data.get('text')

        try:
            task = TaskORM.objects.get(pk=task_id)
            user = UserORM.objects.get(pk=user_id)
        except (TaskORM.DoesNotExist, UserORM.DoesNotExist):
            raise serializers.ValidationError("ID de tarefa ou usuário inválido.")  # noqa: B904

        task_comment = TaskCommentsORM.objects.create(text=text, task=task, user=user)
        return task_comment
