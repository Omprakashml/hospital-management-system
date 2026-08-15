from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient

        fields = [
            'patient_id',
            'first_name',
            'last_name',
            'date_of_birth',
            'gender',
            'blood_group',
            'phone',
            'email',
            'address',
            'emergency_contact_name',
            'emergency_contact_phone',
            'medical_history',
            'allergies',
        ]

        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date'}
            ),

            'address': forms.Textarea(
                attrs={'rows': 3}
            ),

            'medical_history': forms.Textarea(
                attrs={'rows': 3}
            ),

            'allergies': forms.Textarea(
                attrs={'rows': 3}
            ),
        }