from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from commondb.models.user import User
from commondb.models.subscription import Subscription_record

class Command(BaseCommand):
    help = "Monthly batch processing to save information"

    def handle(self, *args, **kwargs):
        #月末の処理
        last_day_of_month = datetime.now().replace(day=1, month=datetime.now().month+1, hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)
        paid_member_ids = User.objects.filter(is_paid_member=True).values_list('id', flat=True)
        
        # 月末の有料会員のIDを取得し、Subscription_recordに保存
        for user_id in paid_member_ids:
            Subscription_record.objects.get_or_create(user_id=user_id, year=last_day_of_month.year, month=last_day_of_month.month)
        
        self.stdout.write(self.style.SUCCESS('Monthly batch processing completed.'))
