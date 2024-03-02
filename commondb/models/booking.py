from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from datetime import date, time
from django.db import models
from .restaurant import Restaurant
from .user import User

def future_date_validator(value):
    if value <= date.today():
        raise ValidationError('予約日は翌日以降を選択してください。')

class Booking(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name="店舗名")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="ユーザー名")
    booking_date = models.DateField(verbose_name="予約日", validators=[future_date_validator])
    booking_time = models.TimeField(verbose_name="予約時間", default=time(18, 0))
    numbers_of_ppl = models.IntegerField(default=0, verbose_name="予約人数", validators=[MaxValueValidator(8)])
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")