from django.db import models
from .user import User
from django.contrib.auth import get_user_model

User = get_user_model()

class Subscription_record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ユーザー')
    year = models.PositiveIntegerField(verbose_name='年')
    month = models.PositiveIntegerField(verbose_name='月')
    is_paid_member = models.BooleanField(default=False, verbose_name='有料会員')

    def __str__(self):
        return f'{self.user.username} - {self.year}/{self.month}'
