from django.contrib import admin
from .models import MedicalRecord


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):

    list_display = (
        'record_id',
        'patient',
        'doctor',
        'visit_date',
        'follow_up_date',
        'created_at',
    )

    list_filter = (
        'visit_date',
        'follow_up_date',
    )

    search_fields = (
        'record_id',
        'patient__patient_id',
        'patient__first_name',
        'patient__last_name',
        'doctor__doctor_id',
        'doctor__first_name',
        'doctor__last_name',
        'diagnosis',
    )

    ordering = (
        '-visit_date',
    )