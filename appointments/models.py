from django.db import models
from patients.models import Patient
from doctors.models import Doctor
from departments.models import Department


class Appointment(models.Model):

    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
        ('No Show', 'No Show'),
    ]

    appointment_id = models.CharField(
        max_length=20,
        unique=True
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='appointments'
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='appointments'
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name='appointments'
    )

    appointment_date = models.DateField()

    appointment_time = models.TimeField()

    reason = models.TextField(
        blank=True
    )

    notes = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Scheduled'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return (
            f"{self.appointment_id} - "
            f"{self.patient.first_name} "
            f"{self.patient.last_name}"
        )

    class Meta:
        ordering = [
            '-appointment_date',
            '-appointment_time'
        ]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    'doctor',
                    'appointment_date',
                    'appointment_time'
                ],
                name='unique_doctor_appointment_time'
            )
        ]