from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):

    SPECIALIZATIONS = [
        ('General Medicine', 'General Medicine'),
        ('Cardiology', 'Cardiology'),
        ('Neurology', 'Neurology'),
        ('Orthopedics', 'Orthopedics'),
        ('Pediatrics', 'Pediatrics'),
        ('Dermatology', 'Dermatology'),
        ('Gynecology', 'Gynecology'),
        ('ENT', 'ENT'),
        ('Ophthalmology', 'Ophthalmology'),
        ('Dentistry', 'Dentistry'),
        ('Psychiatry', 'Psychiatry'),
        ('Other', 'Other'),
    ]

    doctor_id = models.CharField(
        max_length=20,
        unique=True
    )

    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='doctor'
    )

    first_name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=50)

    specialization = models.CharField(
        max_length=50,
        choices=SPECIALIZATIONS
    )
    department = models.ForeignKey(
    'departments.Department',
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='doctors'
    )

    qualification = models.CharField(
        max_length=150
    )

    phone = models.CharField(
        max_length=15
    )

    email = models.EmailField(
        blank=True
    )

    experience_years = models.PositiveIntegerField(
        default=0
    )

    consultation_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    available = models.BooleanField(
        default=True
    )

    joining_date = models.DateField()

    address = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"

    class Meta:
        ordering = ['first_name', 'last_name']