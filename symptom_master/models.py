from django.db import models

# Create your models here.

class SymptomMaster(models.Model):
    id = models.AutoField(primary_key=True)
    symptom_name       = models.CharField(max_length=80)
    
