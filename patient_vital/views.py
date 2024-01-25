from .models import PatientVital
from .serializers import PatientVitalSerializer
from rest_framework import viewsets 

# Create your views here.

class PatientVitalViewSet(viewsets.ModelViewSet): 
    queryset = PatientVital.objects.all()
    serializer_class = PatientVitalSerializer