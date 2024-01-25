from rest_framework import serializers
from .models import Appointment
from django_filters import rest_framework as filters


# Define the serializer

class AppointmentSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient_id', read_only=True)
    class Meta:
        model   = Appointment
        fields  = ('id', 
                'status',
                'appointment_datetime',
                'patient_id',
                'doctor_id',
                'specialization_id',
                'created_by',
                'updated_by',
                'next_appointment',
                'created',
                'updated',
                'patient_name',

                )
        read_only_fields = ('created', 'updated',)
    def to_representation(self, instance):
        """
        Dynamically modify the fields returned by the serializer.
        """
        ret = super().to_representation(instance)

        if not self.context.get('request') or self.context['request'].query_params.get('id'):
            # Return all fields if a single appointment is queried by ID
            return ret

        # Only return patient_id and patient_name for list queries
        else:
            return {
            'id': ret.get('id'),
            'status': ret.get('status'),
            'patient_id': ret.get('patient_id'),
            'patient_name': ret.get('patient_name')
        }

class AppointmentDetailSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient_id', read_only=True)

    class Meta:
        model = Appointment
        fields = (
            'id', 'status', 'appointment_datetime', 'patient_id', 'doctor_id',
            'specialization_id', 'created_by', 'updated_by', 'next_appointment',
            'created', 'updated', 'patient_name',
        )
        read_only_fields = ('created', 'updated',)


class AppointmentFilter(filters.FilterSet):
    appointment_datetime = filters.DateFilter(field_name='appointment_datetime', lookup_expr='date')
    created = filters.DateFilter(field_name='created', lookup_expr='date')
    # 2024-01-05
    class Meta:
        model = Appointment
        fields = ['status', 'created', 'appointment_datetime', 'patient_id' ,'doctor_id']


