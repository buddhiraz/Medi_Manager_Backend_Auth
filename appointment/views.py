from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Appointment
from .serializers import AppointmentSerializer , AppointmentFilter , AppointmentDetailSerializer

# Create your views here.

class AppointmentList(generics.ListCreateAPIView):
    queryset            = Appointment.objects.all()
    serializer_class    = AppointmentSerializer
    filter_backends     = [DjangoFilterBackend]
    filterset_class     = AppointmentFilter
class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset            = Appointment.objects.all()
    serializer_class    = AppointmentDetailSerializer