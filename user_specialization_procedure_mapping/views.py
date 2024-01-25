from .models import UserSpecializationProcedureMapping
from .serializers import UserSpecializationProcedureMappingSerializer
from rest_framework import viewsets # new

# Create your views here.

class UserSpecializationProcedureMappingViewSet(viewsets.ModelViewSet): # new
    queryset = UserSpecializationProcedureMapping.objects.all()
    serializer_class = UserSpecializationProcedureMappingSerializer