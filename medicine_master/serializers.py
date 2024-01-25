from rest_framework import serializers
from .models import MedicineMaster

# Define the serializer

class MedicineMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model   = MedicineMaster
        fields  = ('id', 
                   'medicine_name',
                   'medicine_dosage',
              
                )
    


