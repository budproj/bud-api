from rest_framework.serializers import ModelSerializer
from okr.models import KeyResult

class KeyResultSerializer(ModelSerializer):
    class Meta:
        model = KeyResult
        fields = '__all__'
        read_only = ['id', 'created_at', 'updated_at']