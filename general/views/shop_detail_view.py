from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from commondb.models.restaurant import Restaurant
from commondb.models.review import Review
from commondb.models.booking import Booking
from ..forms import BookingForm
from commondb.models.favorite import Favorite



class ShopTemplatelView(CreateView):
    model = Booking
    #詳細ページのテンプレート名
    template_name = 'general/shop_detail.html'
    # 予約フォーム
    form_class = BookingForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            if self. request.user.is_paid_member:
                context['user_type'] = 'is_paid'
            else:
                context['user_type'] = 'member'
        else:
            context['user_type'] = 'no_member'
        
        # URLから店舗のIDを取得
        restaurant_id = self.kwargs.get('pk') 
        # 店舗詳細
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
        context['restaurant'] = restaurant
        # レビュー
        reviews = Review.objects.filter(restaurant_id=restaurant_id)
        context['reviews'] = reviews
        # 平均評価
        if reviews:
            average_rating = sum(review.rating for review in reviews) / len(reviews)
            context['average_rating'] = round(average_rating, 1)
            context['average_rating_stars'] = '<span style="color: #F57F00;">★</span>' * int(average_rating)
        else:
            context['average_rating'] = None
            context['average_rating_stars'] = None
        
        # 店舗名
        context['form'] = BookingForm(initial={'restaurant': restaurant_id})
        return context

    def form_valid(self, form):
        restaurant_id = self.kwargs.get('pk')
        form.instance.restaurant_id = restaurant_id
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('complete_booking')
