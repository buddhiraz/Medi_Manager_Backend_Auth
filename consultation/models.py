from django.db import models
from user.models import User
from specialization.models import Specialization
from appointment.models import Appointment
from enum import Enum

# Create your models here.


class CONSULTATION_STATUSES(Enum):
    CREATED     = "CR"
    IN_PROGRESS = "IP"
    CANCELLED   = "CN"
    POSTPONED   = "PP"
    CLOSED      = "CL"

class Consultation(models.Model):

    id = models.AutoField(primary_key=True)
    appointment_id  = models.ForeignKey(Appointment ,  on_delete = models.PROTECT)
    created     = models.DateTimeField(auto_now_add=True)
    status          = models.CharField(
                                        max_length  =   2,
                                        choices     =   [(status.value, status.name) for status in CONSULTATION_STATUSES],
                                        default     =   'CR',)

    doctor_id   = models.IntegerField( blank=True , null = True)
    
    updated     = models.DateTimeField(auto_now=True)
    created_by  = models.CharField(max_length = 50, blank=True)
    updated_by  = models.CharField(max_length = 50, blank=True)

    next_appointment = models.DateTimeField(blank=True ,  null =True)
    # template_id = None
    # this to be added soon 
    fee         = models.DecimalField(max_digits=6,decimal_places=2,null=True)
    fee_paid    = models.BooleanField(default = False)

    class Meta:
        ordering = ['created']
        indexes  = [models.Index(fields=['created'])]