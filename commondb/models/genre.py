from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='genre_images', null=True, blank=True)
    
    def __str__(self):
        return self.name
    