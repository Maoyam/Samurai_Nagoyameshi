from django.shortcuts import render
from django.views.generic import CreateView
from commondb.models.company import Company

class CompanyCreateView(CreateView):
    model = Company
    template_name = 'admi/company_form.html'
    fields = ['name', 'address', 'established_date', 'capital', 'number_of_staff']
        
