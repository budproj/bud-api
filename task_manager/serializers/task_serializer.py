from rest_framework.serializers import ModelSerializer, SerializerMethodField
from task_manager.models import Task
from .task_history_serializer import TaskHistorySerializer

class TaskSerializer(ModelSerializer):
    history = TaskHistorySerializer(many=True, read_only=True)
    users_related = SerializerMethodField()
    owner_full_name = SerializerMethodField()
    
    class Meta:
        model = Task
        fields = '__all__'
        read_only = ['team_id', 'created_at', 'update_at', 'deleted_at']
        
    def get_users_related(self, obj):
        data = []
        data.append(self.obj_user(obj.owner))
        for i in obj.support_team:
            data.append(self.obj_user(i))
        return data
    
    def obj_user(self, obj):
        return {
            'id': obj.id,
            'first_name': obj.first_name,
            'last_name': obj.last_name,
            'full_name': f'{obj.first_name} {obj.last_name}',
            'email': obj.email,
            'authz_sub': obj.authz_sub,
            'gender': obj.gender,
            'role': obj.role,
            'picture': obj.picture,
            'created_at': obj.created_at,
            'updated_at': obj.updated_at,
        }
    
    def get_owner_full_name(self, obj):
        if obj.owner:
            return f"{obj.owner.first_name} {obj.owner.last_name}".strip()
        return None