from rest_framework import serializers
from .models import ConsultationInstruction

# Define the serializer

class ConsultationInstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model   = ConsultationInstruction
        fields  = ('id', 
                    'consultation_id', 
                    'instruction',
                )
    


