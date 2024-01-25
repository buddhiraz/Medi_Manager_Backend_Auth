from rest_framework import serializers
from .models import ConsultationSymptom

# Define the serializer

class ConsultationSymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model   = ConsultationSymptom
        fields  = ('id', 
                'consultation_id', 
                'symptom_id',
                )
    


