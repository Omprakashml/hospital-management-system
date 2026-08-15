from django.db import models
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment


class MedicalRecord(models.Model):

    record_id = models.CharField(
        max_length=20,
        unique=True
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='medical_records'
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.PROTECT,
        related_name='medical_records'
    )

    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='medical_record'
    )

    visit_date = models.DateField()

    symptoms = models.TextField()

    diagnosis = models.TextField()

    treatment = models.TextField(
        blank=True
    )

    prescription = models.TextField(
        blank=True
    )

    notes = models.TextField(
        blank=True
    )

    follow_up_date = models.DateField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.record_id} - {self.patient}"

    class Meta:
        ordering = ['-visit_date']