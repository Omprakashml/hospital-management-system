from django.contrib import admin

from .models import Invoice


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):

    list_display = (
        'invoice_number',
        'patient',
        'invoice_date',
        'total_amount_display',
        'amount_paid',
        'balance_due_display',
        'payment_status',
        'payment_method',
    )

    list_filter = (
        'payment_status',
        'payment_method',
        'invoice_date',
    )

    search_fields = (
        'invoice_number',
        'patient__patient_id',
        'patient__first_name',
        'patient__last_name',
    )

    list_editable = (
        'payment_status',
        'payment_method',
    )

    ordering = (
        '-invoice_date',
    )

    @admin.display(description='Total Amount')
    def total_amount_display(self, obj):
        return obj.total_amount

    @admin.display(description='Balance Due')
    def balance_due_display(self, obj):
        return obj.balance_due