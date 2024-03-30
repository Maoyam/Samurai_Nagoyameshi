from django.db import models
from django.dispatch import receiver
from commondb.models.user import User
from django.db.models.signals import post_save

class Upgrade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_bool = models.BooleanField(default=False)
    stripe_checkout_id = models.CharField(max_length=500)
    
@receiver(post_save, sender=User)
def create_user_payment(sender, instance, created, **kwards):
    if created:
        Upgrade.object.create(user=instance)
        