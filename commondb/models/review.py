from django.db import models
from .restaurant import Restaurant
from .user import User
from django.urls import reverse

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, verbose_name="店名", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="ユーザー名", null=True, on_delete=models.CASCADE)
    visit_date = models.DateField(verbose_name="訪問日")
    rating = models.IntegerField(choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')], verbose_name="評価")
    comment = models.TextField(verbose_name="コメント")
    image1 = models.ImageField(upload_to='review_images/', null=True, blank=True, verbose_name="画像")
    image2 = models.ImageField(upload_to='review_images/', null=True, blank=True, verbose_name="画像")
    image3 = models.ImageField(upload_to='review_images/', null=True, blank=True, verbose_name="画像")


    def get_absolute_url(self):
         return reverse('mypage_review_detail', kwargs={'pk': self.pk})
    
    