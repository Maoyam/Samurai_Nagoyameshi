from commondb.models.subscription import Subscription_record
from django.views.generic import ListView


class SubscriptionRecordListView(ListView):
    model = Subscription_record
    template_name = 'admi/subscription_records.html'
    context_object_name = 'monthly_data'

    def get_queryset(self):
        queryset = super().get_queryset()

        # 年のフィルタリング
        year = self.request.GET.get('year')
        if year:
            queryset = queryset.filter(year=year)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 年の選択肢を取得
        context['years'] = Subscription_record.objects.order_by().values_list('year', flat=True).distinct()
        
        # 選択された年を取得し、フィルターのデフォルト値として設定
        selected_year = self.request.GET.get('year')
        context['selected_year'] = selected_year

        # 月ごとの有料会員数と売上合計を取得
        monthly_data = []
        for month in range(1, 13):
            monthly_records = Subscription_record.objects.filter(year=selected_year, month=month)
            member_count = monthly_records.filter(is_paid_member=True).count()
            total_sales = member_count * 300  # 月額代金は300円
            member_count_display = '-' if member_count == 0 else member_count
            total_sales_display = '-' if total_sales == 0 else total_sales
            monthly_data.append((month, member_count_display, total_sales_display))
        context['monthly_data'] = monthly_data

        return context