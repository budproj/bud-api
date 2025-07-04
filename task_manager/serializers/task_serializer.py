from rest_framework.serializers import ModelSerializer, SerializerMethodField
from okr.serializers.key_result_serializer import KeyResultSerializer
from task_manager.models import Task
from user.models import User
from .task_history_serializer import TaskHistorySerializer

class TaskSerializer(ModelSerializer):    
    class Meta:
        model = Task
        fields = '__all__'
        read_only = ['created_at', 'update_at']
        
    def save(self, **kwargs):
        request = self.context.get('request')
        usuario_logado = None
        if request and request.session['user']:
            usuario_logado = request.session['user']
        kwargs['usuario_logado'] = usuario_logado
        return super().save(**kwargs)

    def create(self, validated_data):
        usuario_para_modelo = validated_data.pop('usuario_logado', None)

        instance = self.Meta.model(**validated_data)
        instance.save(usuario_logado=usuario_para_modelo)
        return instance

    def update(self, instance, validated_data):
        usuario_para_modelo = validated_data.pop('usuario_logado', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save(usuario_logado=usuario_para_modelo)
        return instance
    
class TaskReadSerializer(ModelSerializer):
    history = TaskHistorySerializer(many=True, read_only=True)
    users_related = SerializerMethodField()
    support_team = SerializerMethodField()
    owner_full_name = SerializerMethodField()
    key_result = KeyResultSerializer(read_only=True)
    
    class Meta:
        model = Task
        fields = '__all__'
        read_only = '__all__'
        
    def get_users_related(self, obj):
        data = []
        
        if obj.owner:
            data.append(self.obj_user(obj.owner))
    
        if obj.support_team:
            users = User.objects.filter(id__in=obj.support_team)
            for user in users:
                data.append(self.obj_user(user))
    
        return data
    
    def get_support_team(self, obj):
        data = []
    
        if obj.support_team:
            users = User.objects.filter(id__in=obj.support_team)
            for user in users:
                data.append(self.obj_user(user))
    
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