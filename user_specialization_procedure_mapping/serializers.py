from rest_framework import serializers
from .models import UserSpecializationProcedureMapping

# Define the serializer

class  UserSpecializationProcedureMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model   = UserSpecializationProcedureMapping
        fields  = ('id', 
                   'procedure_id',
                   'specialization_id',
                   'user_id', 
                   )
    
    


