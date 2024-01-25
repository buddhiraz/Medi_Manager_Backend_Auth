from .models import ConsultationInstruction
from .serializers import ConsultationInstructionSerializer
from rest_framework import viewsets 

# Create your views here.

class ConsultationInstructionViewSet(viewsets.ModelViewSet): 
    queryset = ConsultationInstruction.objects.all()
    serializer_class = ConsultationInstructionSerializer