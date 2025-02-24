from rest_framework.serializers import ModelSerializer
from okr.models import Cycle

class CycleSerializer(ModelSerializer):
    class Meta:
        model = Cycle
        fields = '__all__'
        
    