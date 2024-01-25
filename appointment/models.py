from django.db import models
from user.models import User
from specialization.models import Specialization

from enum import Enum

# Create your models here.

class APPOINTMENT_STATUSES(Enum):
    CREATED     = "CR"
    IN_PROGRESS = "IP"
    CANCELLED   = "CN"
    POSTPONED   = "PP"
    CLOSED      = "CL"



class Appointment(models.Model):

    id = models.AutoField(primary_key=True)
    appointment_datetime = models.DateTimeField(blank=True,null = True)
    # ^ can be filtered only using date --  in this format >> { 2024-01-05 }
    status          = models.CharField(
                                        max_length  =   2,
                                        choices     =   [(status.value, status.name) for status in APPOINTMENT_STATUSES],
                                        default     =   'CR',
                                    )
    doctor_id       = models.IntegerField(blank=True)
    patient_id      = models.ForeignKey(User, on_delete=models.PROTECT)
    specialization_id  = models.ForeignKey(Specialization, on_delete=models.PROTECT)

    created_by      = models.CharField(max_length = 50, blank=True)
    created         = models.DateTimeField(auto_now_add=True)
    # ^ can be filtered only using date --  in this format >> { 2024-01-05 }
    updated         = models.DateTimeField(auto_now=True)
    updated_by      = models.CharField(max_length = 50,blank=True)

    next_appointment = models.DateTimeField(blank=True , null = True )

    class Meta:
        ordering    = ['created']
        indexes     = [models.Index(fields=['created'])]
