from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):

    list_display = (
        'doctor_id',
        'first_name',
        'last_name',
        'specialization',
        'qualification',
        'experience_years',
        'consultation_fee',
        'available',
    )

    list_filter = (
        'specialization',
        'available',
        'joining_date',
    )

    search_fields = (
        'doctor_id',
        'first_name',
        'last_name',
        'phone',
        'email',
        'qualification',
    )

    list_editable = (
        'available',
        'consultation_fee',
    )

    ordering = (
        'first_name',
        'last_name',
    )