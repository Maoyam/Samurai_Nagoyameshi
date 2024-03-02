from django.db import models
from .restaurant import Restaurant
from .user import User

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    visit_date = models.DateField()
    rating = models.IntegerField(choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')])
    comment = models.TextField()
    image1 = models.ImageField(upload_to='review_images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='review_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='review_images/', null=True, blank=True)

    
    