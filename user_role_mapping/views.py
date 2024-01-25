from .models import UserRoleMapping
from .serializers import UserRoleMappingSerializer
from rest_framework import viewsets # new

# Create your views here.

class UserRoleMappingViewSet(viewsets.ModelViewSet): # new
    queryset = UserRoleMapping.objects.all()
    serializer_class = UserRoleMappingSerializer