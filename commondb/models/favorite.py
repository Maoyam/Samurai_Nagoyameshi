from django.db import models
from .restaurant import Restaurant
from .user import User


class Favorite(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name="店舗名")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="ユーザー名")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")