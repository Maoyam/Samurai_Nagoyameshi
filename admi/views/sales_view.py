from django.shortcuts import render
from django.views.generic import ListView
from commondb.models.sale import Sale
from django.db.models import Sum, Count
from django.utils import timezone

class SaleListView(ListView):
    model = Sale
    template_name = 'admi/sale_list.html'
    context_object_name = 'sales'

    def get_queryset(self):
        queryset = super().get_queryset()
        year = self.request.GET.get('year')
        month = self.request.GET.get('month')

        if year and month:
            queryset = queryset.filter(month=timezone.datetime(int(year), int(month), 1))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_sales'] = self.get_queryset().aggregate(total_sales=Sum('total_sales'))['total_sales'] or 0
        context['total_paid_members'] = self.get_queryset().aggregate(total_paid_members=Sum('paid_member_count'))['total_paid_members'] or 0
        return context
