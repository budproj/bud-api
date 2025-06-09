from rest_framework.serializers import ModelSerializer, SerializerMethodField
from user.models import User

class UserSerializer(ModelSerializer):
    full_name = SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'
        
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip()