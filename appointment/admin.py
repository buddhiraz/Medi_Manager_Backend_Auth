from django.contrib import admin
from .models import Appointment, APPOINTMENT_STATUSES

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'appointment_datetime', 'status', 'doctor_id', 'patient_id', 'specialization_id', 'created_by', 'created', 'updated', 'updated_by', 'next_appointment')
    list_filter = ('status', 'specialization_id')
    search_fields = ('id', 'created_by', 'updated_by')

    # Customize the display of the 'status' field using a function
    def display_status(self, obj):
        return dict(APPOINTMENT_STATUSES)[obj.status]
    display_status.short_description = 'Status'

admin.site.register(Appointment, AppointmentAdmin)
