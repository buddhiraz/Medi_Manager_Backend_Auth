from rest_framework import serializers
from .models import TemplateMaster

# Define the serializer

class TemplateMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model   = TemplateMaster
        fields  = ('id', 
                'template_path', 
                )
    


