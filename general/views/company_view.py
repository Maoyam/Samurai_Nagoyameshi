from typing import Any
from django.views.generic import DetailView
from commondb.models.company import Company

class CompanyDetailView(DetailView):
    model = Company
    template_name = "general/company.html"
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = self.get_object()
        return context