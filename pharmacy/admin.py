from django.contrib import admin

from .models import Medicine, Prescription


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):

    list_display = (
        'medicine_id',
        'name',
        'generic_name',
        'category',
        'batch_number',
        'expiry_date',
        'stock_quantity',
        'minimum_stock_level',
        'selling_price',
        'is_active',
        'stock_status',
        'expiry_status',
    )

    list_filter = (
        'category',
        'is_active',
        'expiry_date',
    )

    search_fields = (
        'medicine_id',
        'name',
        'generic_name',
        'batch_number',
        'manufacturer',
        'supplier',
    )

    list_editable = (
        'stock_quantity',
        'is_active',
    )

    ordering = (
        'name',
    )

    @admin.display(description='Stock Status')
    def stock_status(self, obj):
        if obj.is_low_stock:
            return 'LOW STOCK'
        return 'OK'

    @admin.display(description='Expiry Status')
    def expiry_status(self, obj):
        if obj.is_expired:
            return 'EXPIRED'
        return 'VALID'


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):

    list_display = (
        'prescription_id',
        'medical_record',
        'medicine',
        'dosage',
        'frequency',
        'duration_days',
        'quantity',
        'prescribed_date',
    )

    list_filter = (
        'prescribed_date',
        'medicine__category',
    )

    search_fields = (
        'prescription_id',
        'medicine__name',
        'medical_record__record_id',
        'medical_record__patient__first_name',
        'medical_record__patient__last_name',
    )

    ordering = (
        '-prescribed_date',
    )