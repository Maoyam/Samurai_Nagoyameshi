from django.db import models
from commondb.models.user import User
from django.utils import timezone

class StripeCustomer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    stripeCustomerId = models.CharField(max_length=255)
    stripeSubscriptionId = models.CharField(max_length=255)
    regist_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username
        