from django.shortcuts import render
from django.views.generic.edit import UpdateView
from commondb.models.company import Company

class CompanyUpdateView(UpdateView):
    model = Company
    template_name = 'admi/company_edit.html'
    fields = ['name', 'address', 'established_date', 'capital', 'number_of_staff']
        
