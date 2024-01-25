from django.db import models

# Create your models here.

class TemplateMaster(models.Model):
    id = models.AutoField(primary_key=True)
    template_path  = models.CharField(max_length=50 ,  blank=True)
    #

