from rest_framework import generics
from .models import Consultation
from .serializers import ConsultationSerializer

# Create your views here.

class ConsultationList(generics.ListCreateAPIView):
    queryset            = Consultation.objects.all()
    serializer_class    = ConsultationSerializer
class ConsultationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset        = Consultation.objects.all()
    serializer_class = ConsultationSerializer
