from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone


class Medicine(models.Model):

    medicine_id = models.CharField(
        max_length=20,
        unique=True
    )

    name = models.CharField(
        max_length=150
    )

    generic_name = models.CharField(
        max_length=150,
        blank=True
    )

    category = models.CharField(
        max_length=100
    )

    manufacturer = models.CharField(
        max_length=150,
        blank=True
    )

    batch_number = models.CharField(
        max_length=50
    )

    expiry_date = models.DateField()

    purchase_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))]
    )

    selling_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))]
    )

    stock_quantity = models.PositiveIntegerField(
        default=0
    )

    minimum_stock_level = models.PositiveIntegerField(
        default=10
    )

    supplier = models.CharField(
        max_length=150,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    @property
    def is_expired(self):
        return self.expiry_date < timezone.localdate()

    @property
    def is_low_stock(self):
        return self.stock_quantity <= self.minimum_stock_level

    def __str__(self):
        return f"{self.name} ({self.batch_number})"

    class Meta:
        ordering = ['name']

class Prescription(models.Model):

    prescription_id = models.CharField(
        max_length=20,
        unique=True
    )

    medical_record = models.ForeignKey(
        'medical_records.MedicalRecord',
        on_delete=models.CASCADE,
        related_name='prescriptions'
    )

    medicine = models.ForeignKey(
        Medicine,
        on_delete=models.PROTECT,
        related_name='prescriptions'
    )

    dosage = models.CharField(
        max_length=100
    )

    frequency = models.CharField(
        max_length=100
    )

    duration_days = models.PositiveIntegerField()

    quantity = models.PositiveIntegerField()

    instructions = models.TextField(
        blank=True
    )

    prescribed_date = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.prescription_id} - {self.medicine.name}"

    class Meta:
        ordering = ['-prescribed_date']