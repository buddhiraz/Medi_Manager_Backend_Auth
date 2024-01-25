from rest_framework import serializers
from .models import Consultation

# Define the serializer

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Consultation
        fields  = ('id',  
                'appointment_id',
                'created',
                'status',
                'doctor_id',
                'updated',
                'updated_by',

                'fee',
                'fee_paid',
                'next_appointment',

                )
    