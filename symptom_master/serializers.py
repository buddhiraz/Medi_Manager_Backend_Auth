from rest_framework import serializers
from .models import SymptomMaster

# Define the serializer

class  SymptomMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model   = SymptomMaster
        fields  = ('id', 
                   'symptom_name',
                )
    


