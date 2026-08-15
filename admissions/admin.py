from django.contrib import admin

from .models import Ward, Room, Bed, Admission


@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):

    list_display = (
        'ward_id',
        'name',
        'ward_type',
        'floor',
        'is_active',
    )

    list_filter = (
        'ward_type',
        'floor',
        'is_active',
    )

    search_fields = (
        'ward_id',
        'name',
    )


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    list_display = (
        'room_number',
        'ward',
        'room_type',
        'floor',
        'daily_charge',
        'is_active',
    )

    list_filter = (
        'room_type',
        'floor',
        'is_active',
    )

    search_fields = (
        'room_number',
        'ward__name',
    )


@admin.register(Bed)
class BedAdmin(admin.ModelAdmin):

    list_display = (
        'bed_number',
        'room',
        'status',
    )

    list_filter = (
        'status',
        'room__ward',
    )

    search_fields = (
        'bed_number',
        'room__room_number',
    )

    list_editable = (
        'status',
    )


@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):

    list_display = (
        'admission_id',
        'patient',
        'doctor',
        'bed',
        'admission_date',
        'discharge_date',
        'status',
    )

    list_filter = (
        'status',
        'admission_date',
        'bed__room__ward',
    )

    search_fields = (
        'admission_id',
        'patient__patient_id',
        'patient__first_name',
        'patient__last_name',
        'doctor__doctor_id',
        'doctor__first_name',
        'doctor__last_name',
        'bed__bed_number',
    )

    ordering = (
        '-admission_date',
    )