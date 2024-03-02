# forms.py
from django import forms
from commondb.models.company import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'established_date', 'capital', 'number_of_staff']
        widgets = {
            'established_date': forms.DateInput(attrs={'type': 'date'}),
        }
