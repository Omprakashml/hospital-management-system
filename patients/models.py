from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):

    BLOOD_GROUPS = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    patient_id = models.CharField(
        max_length=20,
        unique=True
    )

    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='patient'
    )

    first_name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=50)

    date_of_birth = models.DateField()

    gender = models.CharField(
        max_length=20,
        choices=[
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other'),
        ]
    )

    blood_group = models.CharField(
        max_length=3,
        choices=BLOOD_GROUPS,
        blank=True
    )

    phone = models.CharField(max_length=15)

    email = models.EmailField(blank=True)

    address = models.TextField()

    emergency_contact_name = models.CharField(
        max_length=100
    )

    emergency_contact_phone = models.CharField(
        max_length=15
    )

    medical_history = models.TextField(
        blank=True
    )

    allergies = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.patient_id} - {self.first_name} {self.last_name}"