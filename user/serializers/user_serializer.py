from rest_framework.serializers import ModelSerializer, SerializerMethodField
from user.models import UserORM

class UserSerializer(ModelSerializer):
    full_name = SerializerMethodField()

    class Meta:
        model = UserORM
        fields = '__all__'
        
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip()