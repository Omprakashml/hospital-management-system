from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PatientForm
from .models import Patient


@login_required
def patient_list(request):

    query = request.GET.get('q', '').strip()

    patients = Patient.objects.all().order_by('-created_at')

    if query:
        patients = patients.filter(
            Q(patient_id__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query)
        )

    context = {
        'patients': patients,
        'query': query,
        'total_patients': Patient.objects.count(),
    }

    return render(
        request,
        'patients/patient_list.html',
        context
    )


@login_required
def patient_detail(request, pk):

    patient = get_object_or_404(
        Patient,
        pk=pk
    )

    return render(
        request,
        'patients/patient_detail.html',
        {'patient': patient}
    )


@login_required
def patient_create(request):

    if request.method == 'POST':

        form = PatientForm(request.POST)

        if form.is_valid():

            patient = form.save()

            messages.success(
                request,
                f'Patient {patient.first_name} {patient.last_name} added successfully.'
            )

            return redirect(
                'patient_detail',
                pk=patient.pk
            )

    else:

        form = PatientForm()

    return render(
        request,
        'patients/patient_form.html',
        {
            'form': form,
            'title': 'Add Patient',
        }
    )


@login_required
def patient_update(request, pk):

    patient = get_object_or_404(
        Patient,
        pk=pk
    )

    if request.method == 'POST':

        form = PatientForm(
            request.POST,
            instance=patient
        )

        if form.is_valid():

            patient = form.save()

            messages.success(
                request,
                'Patient information updated successfully.'
            )

            return redirect(
                'patient_detail',
                pk=patient.pk
            )

    else:

        form = PatientForm(
            instance=patient
        )

    return render(
        request,
        'patients/patient_form.html',
        {
            'form': form,
            'title': 'Edit Patient',
            'patient': patient,
        }
    )


@login_required
def patient_delete(request, pk):

    patient = get_object_or_404(
        Patient,
        pk=pk
    )

    if request.method == 'POST':

        patient_name = (
            f'{patient.first_name} {patient.last_name}'
        )

        patient.delete()

        messages.success(
            request,
            f'Patient {patient_name} deleted successfully.'
        )

        return redirect('patient_list')

    return render(
        request,
        'patients/patient_confirm_delete.html',
        {'patient': patient}
    )