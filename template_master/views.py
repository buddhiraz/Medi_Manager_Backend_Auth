from .models import TemplateMaster
from .serializers import TemplateMasterSerializer
from rest_framework import viewsets 

# Create your views here.

class TemplateMasterViewSet(viewsets.ModelViewSet): # new
    queryset = TemplateMaster.objects.all()
    serializer_class = TemplateMasterSerializer