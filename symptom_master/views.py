from .models import SymptomMaster
from .serializers import SymptomMasterSerializer
from rest_framework import viewsets # new

# Create your views here.

class SymptomMasterViewSet(viewsets.ModelViewSet): # new
    queryset = SymptomMaster.objects.all()
    serializer_class = SymptomMasterSerializer