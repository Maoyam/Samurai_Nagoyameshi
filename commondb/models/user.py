from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class User(AbstractUser):
    is_paid_member = models.BooleanField(verbose_name='有料会員', default=False)
    is_manage_member = models.BooleanField(verbose_name='管理者', default=False)
    
    # 新規作成・編集完了時のリダイレクト先
    def get_absolute_url(self):
         return reverse('top')
     
     
    class Meta:
        verbose_name = 'ユーザー'
        verbose_name_plural = 'ユーザー一覧'
        
    

        