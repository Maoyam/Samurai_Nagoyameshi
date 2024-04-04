from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from models.user import User

class Command(BaseCommand):
    help = "Monthly batch processing to save information"

    def handle(self, *args, **kwargs):
        # ここに月末の処理を記述します
        last_day_of_month = datetime.now().replace(day=1, month=datetime.now().month+1, hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)
        paid_members = User.objects.filter(is_paid_member=True).values_list('id', flat=True)
        # 月末の有料会員のIDを取得し、適切な処理を行います
        self.stdout.write(self.style.SUCCESS('Monthly batch processing completed.'))
