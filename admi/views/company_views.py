from django.views.generic.edit import UpdateView
from commondb.models.company import Company
from ..views.login_permission_view import AdmiRequiredView

class CompanyUpdateView(AdmiRequiredView, UpdateView):
    model = Company
    template_name = 'admi/company_edit.html'
    fields = ['name', 'address', 'established_date', 'capital', 'number_of_staff']
        
