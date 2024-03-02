from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_paid_member = models.BooleanField(verbose_name='有料会員', default=False)
    is_manage_member = models.BooleanField(verbose_name='管理者', default=False)
    
    class Meta:
        verbose_name = 'ユーザー'
        verbose_name_plural = 'ユーザー一覧'  