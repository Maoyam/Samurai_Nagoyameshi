# views.py

from django.views.generic import TemplateView
from datetime import datetime
from commondb.models.user import User
from commondb.models.sale import Sales

class SalesSummaryView(TemplateView):
    template_name = 'admi/sales_summary.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['years'] = range(2020, datetime.now().year + 1)
        context['months'] = range(1, 13)

        selected_year = self.request.GET.get('year')
        selected_month = self.request.GET.get('month')

        context['selected_year'] = int(selected_year) if selected_year else None
        context['selected_month'] = int(selected_month) if selected_month else None

        total_sales = 0
        paid_member_count = 0

        if selected_year and selected_month:
            total_sales, paid_member_count = Sales.get_sales_summary(int(selected_year), int(selected_month))
            
        total_sales = paid_member_count * 300

        context['total_sales'] = total_sales
        context['paid_member_count'] = paid_member_count

        return context
