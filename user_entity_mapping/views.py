from .models import UserEntityMapping
from .serializers import UserEntityMappingSerializer
from rest_framework import viewsets # new

# Create your views here.

class  UserEntityMappingViewSet(viewsets.ModelViewSet): # new
    queryset = UserEntityMapping.objects.all()
    serializer_class = UserEntityMappingSerializer