from django.db import models
from commondb.models.user import User
from django.utils import timezone
from django.db.models import Sum
from datetime import datetime


class Sales(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    date = models.DateField(default=datetime.now)

    @classmethod
    def get_sales_summary(cls, year, month):
        start_date = datetime(year, month, 1)
        end_date = datetime(year, month, 1).replace(day=1, month=month+1) if month < 12 else datetime(year+1, 1, 1)
        sales_data = cls.objects.filter(date__range=[start_date, end_date])
        total_sales = sales_data.aggregate(total=Sum('amount'))['total']
        paid_member_count = User.objects.filter(is_paid_member=True).count()
        return total_sales, paid_member_count