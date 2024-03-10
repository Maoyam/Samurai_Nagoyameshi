from django.db import models

class Reguration(models.Model):
    name = models.CharField(max_length=100,default="", verbose_name="規約名")
    text = models.TextField(max_length=10000,default="", verbose_name="規約本文")
    
    def __str__(self):
        return self.name