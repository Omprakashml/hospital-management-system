from django.db import models


class Department(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    code = models.CharField(
        max_length=10,
        unique=True
    )

    description = models.TextField(
        blank=True
    )

    location = models.CharField(
        max_length=100,
        blank=True
    )

    phone = models.CharField(
        max_length=15,
        blank=True
    )

    head_of_department = models.ForeignKey(
        'doctors.Doctor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='headed_department'
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

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
        ordering = ['name']