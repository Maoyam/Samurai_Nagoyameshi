from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Sale(models.Model):
    month = models.DateField(verbose_name='年月', unique=True)
    total_sales = models.DecimalField(verbose_name='合計売上', max_digits=10, decimal_places=2, default=300.00)
    paid_member_count = models.IntegerField(verbose_name='有料会員数')

    def __str__(self):
        return self.month.strftime('%Y年%m月')