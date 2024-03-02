from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name='会社名')
    address = models.CharField(max_length=100, verbose_name='所在地')
    established_date = models.DateField(verbose_name='設立日')
    capital = models.CharField(max_length=100, verbose_name='資本金')
    number_of_staff = models.CharField(max_length=100, verbose_name='従業員数')
    
    def __str__(self):
        return self.name
    