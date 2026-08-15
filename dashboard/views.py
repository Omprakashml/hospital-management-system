from datetime import date

from django.contrib.auth.decorators import login_required
from django.db import models
from django.shortcuts import render

from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment
from admissions.models import Bed, Admission
from pharmacy.models import Medicine
from billing.models import Invoice


@login_required
def dashboard(request):

    today = date.today()

    total_patients = Patient.objects.count()

    total_doctors = Doctor.objects.count()

    total_appointments = Appointment.objects.filter(
        appointment_date=today
    ).count()

    available_beds = Bed.objects.filter(
        status='Available'
    ).count()

    occupied_beds = Bed.objects.filter(
        status='Occupied'
    ).count()

    total_beds = Bed.objects.count()

    active_admissions = Admission.objects.filter(
        status='Admitted'
    ).count()

    low_stock_medicines = Medicine.objects.filter(
        is_active=True,
        stock_quantity__lte=models.F('minimum_stock_level')
    ).count()

    pending_bills = Invoice.objects.filter(
        payment_status__in=['Pending', 'Partially Paid']
    ).count()

    recent_appointments = Appointment.objects.select_related(
        'patient',
        'doctor',
        'department'
    ).order_by(
        '-appointment_date',
        '-appointment_time'
    )[:5]

    recent_admissions = Admission.objects.select_related(
        'patient',
        'doctor',
        'bed'
    ).order_by(
        '-admission_date'
    )[:5]

    context = {
        'total_patients': total_patients,
        'total_doctors': total_doctors,
        'total_appointments': total_appointments,
        'available_beds': available_beds,
        'occupied_beds': occupied_beds,
        'total_beds': total_beds,
        'active_admissions': active_admissions,
        'low_stock_medicines': low_stock_medicines,
        'pending_bills': pending_bills,
        'recent_appointments': recent_appointments,
        'recent_admissions': recent_admissions,
        'today': today,
    }

    return render(
        request,
        'dashboard/dashboard.html',
        context
    )