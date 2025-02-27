from decimal import Decimal
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from okr.models import KeyResult, KeyResultCheckIn

class KeyResultSerializer(ModelSerializer):
    last_checkin = SerializerMethodField()
    
    class Meta:
        model = KeyResult
        fields = '__all__'
        read_only = ['id', 'created_at', 'updated_at']
        
    def get_last_checkin(self, obj):
        last_checkin = KeyResultCheckIn.objects.filter(key_result=obj).order_by('created_at').last()
        if last_checkin:
            return self.obj_check_in(obj, last_checkin)
        return None
        
    
    def obj_check_in(
            self,              
            key_result: KeyResult, 
            checkin: KeyResultCheckIn
        ):
        progress = Decimal((checkin.value * 100)) / key_result.goal 

        return {
            'progress': progress,
            'value': checkin.value,
            'confidence': checkin.confidence,
            'comment': checkin.comment,
            'user': checkin.user_id, # type: ignore - Campo gerado automaticamente no django
            'parent': checkin.parent,
        }
