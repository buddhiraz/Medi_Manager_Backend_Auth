from django.db import models
from consultation.models import Consultation
from medicine_master.models import MedicineMaster

from enum import Enum

# Create your models here.
class MEDICINE_TIMING(Enum):
    MORNING     = 'MN'
    MIDDAY      = 'MD'
    NOON        = 'NN'
    AFTERNOON   = 'AF'
    EVENING     = 'EV'
    NIGHT       = 'NT'

class MEDICINE_TIMING_FOOD_WISE(Enum):
    AFTER_FOOD  = 'AF'
    BEFORE_FOOD = 'BF'
    

class ConsultationMedicine(models.Model):
    id = models.AutoField(primary_key=True)
    consultation_id = models.ForeignKey(Consultation , on_delete= models.PROTECT)
    medicine_id     = models.ForeignKey(MedicineMaster , on_delete= models.PROTECT)

    medicine_dosage = models.DecimalField(max_digits=2, 
                                          decimal_places=1, #!Keeping decimal for half-tablet (case : kids)
                                          default=1.0) 

    medicine_timing = models.CharField(
                                        max_length  =   2,
                                        choices     =   [(time.value, time.name) for time in MEDICINE_TIMING],
                                        default     =   'MN',  # Morning is the default time
                                    )
    medicine_timing_food = models.CharField(
                                        max_length  =   2,
                                        choices     =   [(time_f.value, time_f.name) for time_f in MEDICINE_TIMING_FOOD_WISE],
                                        default     =   'AF',  # After Food is the default timing
                                    )
    instruction     = models.TextField(max_length=200 , blank=True)


