from django.db import models
from patients.models import Patient
from doctors.models import Doctor


class Ward(models.Model):

    WARD_TYPES = [
        ('General', 'General'),
        ('ICU', 'ICU'),
        ('Emergency', 'Emergency'),
        ('Private', 'Private'),
        ('Semi-Private', 'Semi-Private'),
        ('Pediatric', 'Pediatric'),
        ('Maternity', 'Maternity'),
    ]

    ward_id = models.CharField(
        max_length=20,
        unique=True
    )

    name = models.CharField(
        max_length=100
    )

    ward_type = models.CharField(
        max_length=30,
        choices=WARD_TYPES
    )

    floor = models.PositiveIntegerField()

    description = models.TextField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.ward_id} - {self.name}"

    class Meta:
        ordering = ['floor', 'name']


class Room(models.Model):

    ROOM_TYPES = [
        ('General', 'General'),
        ('Private', 'Private'),
        ('Semi-Private', 'Semi-Private'),
        ('ICU', 'ICU'),
        ('Emergency', 'Emergency'),
    ]

    room_number = models.CharField(
        max_length=20,
        unique=True
    )

    ward = models.ForeignKey(
        Ward,
        on_delete=models.PROTECT,
        related_name='rooms'
    )

    room_type = models.CharField(
        max_length=30,
        choices=ROOM_TYPES
    )

    floor = models.PositiveIntegerField()

    daily_charge = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f"Room {self.room_number}"

    class Meta:
        ordering = ['floor', 'room_number']


class Bed(models.Model):

    BED_STATUS = [
        ('Available', 'Available'),
        ('Occupied', 'Occupied'),
        ('Maintenance', 'Maintenance'),
    ]

    bed_number = models.CharField(
        max_length=20,
        unique=True
    )

    room = models.ForeignKey(
        Room,
        on_delete=models.PROTECT,
        related_name='beds'
    )

    status = models.CharField(
        max_length=20,
        choices=BED_STATUS,
        default='Available'
    )

    def __str__(self):
        return f"Bed {self.bed_number} - Room {self.room.room_number}"

    class Meta:
        ordering = ['room', 'bed_number']


class Admission(models.Model):

    ADMISSION_STATUS = [
        ('Admitted', 'Admitted'),
        ('Discharged', 'Discharged'),
        ('Transferred', 'Transferred'),
    ]

    admission_id = models.CharField(
        max_length=20,
        unique=True
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.PROTECT,
        related_name='admissions'
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.PROTECT,
        related_name='admissions'
    )

    bed = models.ForeignKey(
        Bed,
        on_delete=models.PROTECT,
        related_name='admissions'
    )

    admission_date = models.DateTimeField()

    discharge_date = models.DateTimeField(
        null=True,
        blank=True
    )

    reason = models.TextField()

    diagnosis = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=ADMISSION_STATUS,
        default='Admitted'
    )

    notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.admission_id} - {self.patient}"

    class Meta:
        ordering = ['-admission_date']