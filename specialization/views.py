from django.shortcuts import render
from rest_framework import generics
from .models import Specialization
from .serializers import SpecializationSerializer

# Create your views here.

class SpecializationList(generics.ListCreateAPIView):
    queryset            = Specialization.objects.all()
    serializer_class    = SpecializationSerializer
class SpecializationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset        = Specialization.objects.all()
    serializer_class = SpecializationSerializer