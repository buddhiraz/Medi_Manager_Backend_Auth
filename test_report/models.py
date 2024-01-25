from django.db import models
from user.models  import User
from appointment.models import Appointment

# Create your models here.

class TestReport(models.Model):
    id                  = models.AutoField(primary_key=True)
    user_id             = models.ForeignKey(User, on_delete=models.PROTECT)
    appointment_id      = models.ForeignKey(Appointment, on_delete=models.PROTECT,
                                            blank=True)
    # document_path       = models.FilePathField(blank=True)

