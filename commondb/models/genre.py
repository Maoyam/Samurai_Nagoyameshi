from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="ジャンル名")
    image = models.ImageField(upload_to='genre_images', null=True, blank=True, verbose_name="バナー画像")
    
    def __str__(self):
        return self.name
    