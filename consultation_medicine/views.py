from .models import ConsultationMedicine
from .serializers import ConsultationMedicineSerializer
from rest_framework import viewsets 

# Create your views here.

class ConsultationMedicineViewSet(viewsets.ModelViewSet): 
    queryset = ConsultationMedicine.objects.all()
    serializer_class = ConsultationMedicineSerializer