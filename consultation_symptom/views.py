from .models import ConsultationSymptom
from .serializers import ConsultationSymptomSerializer
from rest_framework import viewsets 

# Create your views here.

class ConsultationSymptomViewSet(viewsets.ModelViewSet): 
    queryset = ConsultationSymptom.objects.all()
    serializer_class = ConsultationSymptomSerializer