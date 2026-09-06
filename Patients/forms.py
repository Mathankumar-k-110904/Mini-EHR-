from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = [
            'name',
            'age',
            'gender',
            'phone',
            'email',
            'address',
            'blood_group',
            'allergies',
            'medical_history',
            'medications',
        ]

        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'allergies': forms.Textarea(attrs={'rows': 3}),
            'medical_history': forms.Textarea(attrs={'rows': 3}),
            'medications': forms.Textarea(attrs={'rows': 3}),
        }