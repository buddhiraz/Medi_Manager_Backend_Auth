from django.db import models

# Create your models here.

class MedicineMaster(models.Model):
    id = models.AutoField(primary_key=True)
    medicine_name       = models.CharField(max_length=50)
    medicine_dosage     = models.CharField(max_length=50)