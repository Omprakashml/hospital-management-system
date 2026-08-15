from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):

    list_display = (
        'patient_id',
        'first_name',
        'last_name',
        'gender',
        'blood_group',
        'phone',
        'created_at',
    )

    list_filter = (
        'gender',
        'blood_group',
        'created_at',
    )

    search_fields = (
        'patient_id',
        'first_name',
        'last_name',
        'phone',
        'email',
    )

    ordering = ('-created_at',)