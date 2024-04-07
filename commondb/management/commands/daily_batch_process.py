from django.core.management.base import BaseCommand
from datetime import datetime
from commondb.models.user import User

class Command(BaseCommand):
    help = "Daily batch processing to retrieve information"

    def handle(self, *args, **kwargs):
        date_today = datetime.now().date()
        
        paid_members = User.objects.filter(is_paid_member=True).values_list('id', flat=True)
        
        self.stdout.write(self.style.SUCCESS('Daily batch processing completed.'))
