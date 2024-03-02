from django.db import models
from .genre import Genre
from .area import Area


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    name_alphabet = models.CharField(max_length=100, )
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    time = models.CharField(max_length=100)
    price_low = models.CharField(max_length=5)
    price_high = models.CharField(max_length=5)
    image = models.ImageField(upload_to='restaurant_images', null=True, blank=True)
    information = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
    