from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Subscription_record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ユーザー')
    year = models.PositiveIntegerField(verbose_name='年')
    month = models.PositiveIntegerField(verbose_name='月')
    
    class Meta:
        unique_together = ('user', 'year', 'month')  # 重複を許さないように設定

    def __str__(self):
        return f'{self.user.username} - {self.year}/{self.month}'
