from django.db import models
from consultation.models import Consultation
from symptom_master.models import SymptomMaster

# Create your models here.
class ConsultationSymptom(models.Model):
    id = models.AutoField(primary_key=True)
    consultation_id  = models.ForeignKey(Consultation , on_delete= models.PROTECT)
    symptom_id       = models.ForeignKey(SymptomMaster , on_delete= models.PROTECT)
