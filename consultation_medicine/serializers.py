from rest_framework import serializers
from .models import ConsultationMedicine

# Define the serializer

class ConsultationMedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model   = ConsultationMedicine
        fields  = ('id', 
                'consultation_id', 
                'medicine_id',
                'medicine_dosage',
                'medicine_timing',
                'medicine_timing_food',
                'instruction',
                )
    


