from django.db import models
from .genre import Genre
from .area import Area
from django.urls import reverse
from django.core.validators import RegexValidator

class Restaurant(models.Model):
    name = models.CharField(max_length=100, verbose_name="店舗名")
    name_alphabet = models.CharField(max_length=100, validators=[RegexValidator(r'^[a-zA-Z]+$')], verbose_name="店舗名アルファベット表記")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name="カテゴリー")
    address = models.CharField(max_length=100, verbose_name="所在地")
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="エリア")
    phone = models.CharField(max_length=20, verbose_name="電話番号")
    time = models.CharField(max_length=100, verbose_name="営業時間")
    price_low = models.CharField(max_length=5 ,verbose_name="下限価格")
    price_high = models.CharField(max_length=5, verbose_name="上限価格")
    image = models.ImageField(upload_to='restaurant_images', null=True, blank=True, verbose_name="画像")
    information = models.TextField(max_length=300, verbose_name="お店の説明")
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('admi:shop_list')
    
    