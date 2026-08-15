from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = (
        'appointment_id',
        'patient',
        'doctor',
        'department',
        'appointment_date',
        'appointment_time',
        'status',
    )

    list_filter = (
        'status',
        'department',
        'appointment_date',
    )

    search_fields = (
        'appointment_id',
        'patient__first_name',
        'patient__last_name',
        'patient__patient_id',
        'doctor__first_name',
        'doctor__last_name',
        'doctor__doctor_id',
    )

    list_editable = (
        'status',
    )

    ordering = (
        '-appointment_date',
        '-appointment_time',
    )