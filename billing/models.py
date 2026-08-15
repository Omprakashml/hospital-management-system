from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from appointments.models import Appointment
from patients.models import Patient


class Invoice(models.Model):

    PAYMENT_STATUS = [
        ('Pending', 'Pending'),
        ('Partially Paid', 'Partially Paid'),
        ('Paid', 'Paid'),
        ('Cancelled', 'Cancelled'),
    ]

    PAYMENT_METHODS = [
        ('Cash', 'Cash'),
        ('Card', 'Card'),
        ('UPI', 'UPI'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Insurance', 'Insurance'),
    ]

    invoice_number = models.CharField(
        max_length=20,
        unique=True
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.PROTECT,
        related_name='invoices'
    )

    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='invoices'
    )

    consultation_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))]
    )

    medicine_charges = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))]
    )

    room_charges = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))]
    )

    other_charges = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))]
    )

    discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))]
    )

    tax = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))]
    )

    amount_paid = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))]
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default='Pending'
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHODS,
        blank=True
    )

    notes = models.TextField(
        blank=True
    )

    invoice_date = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    @property
    def subtotal(self):
        return (
            self.consultation_fee
            + self.medicine_charges
            + self.room_charges
            + self.other_charges
        )

    @property
    def total_amount(self):
        total = self.subtotal - self.discount + self.tax
        return max(total, Decimal('0.00'))

    @property
    def balance_due(self):
        balance = self.total_amount - self.amount_paid
        return max(balance, Decimal('0.00'))

    def __str__(self):
        return f"{self.invoice_number} - {self.patient}"