from django.db.models.query_utils import Q
from rest_framework import serializers

from okr.models import KeyResult
from task_manager.models import Task

class KeyResultTaskSerializer(serializers.ModelSerializer):
    kr_tasks = serializers.SerializerMethodField()
    
    class Meta:
        model = KeyResult
        fields = '__all__'
        read_only = ['id', 'created_at', 'updated_at']
        
    def get_kr_tasks(self, obj):
        user_id = self.context.get('user_selected')
        data = []
        
        tasks = Task.objects.filter(
            (Q(support_team__contains=[user_id]) & Q(key_result__id=obj.id) & Q(deleted_at__isnull=True)) | 
            (Q(owner__id=user_id)) & Q(key_result__id=obj.id) & Q(deleted_at__isnull=True))
        for task in tasks:
            data.append(self.obj_task(task))
        return data
    
    def obj_task(self, obj):
        return {
            "id": str(obj.id),
            "team_id": str(obj.team.id) if obj.team_id else None,
            "owner": str(obj.owner.id),
            "owner_full_name": f"{obj.owner.first_name} {obj.owner.last_name}".strip(), 
            "status": obj.status,
            "title": obj.title,
            "description": obj.description,
            "priority": obj.priority,
            "support_team": obj.support_team
        }
