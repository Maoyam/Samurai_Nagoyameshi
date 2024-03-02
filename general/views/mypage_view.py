from typing import Any
import datetime
from commondb.models.booking import Booking
from commondb.models.review import Review
from commondb.models.favorite import Favorite
from commondb.models.user import User
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class MypageView(LoginRequiredMixin, TemplateView):
    template_name = "general/mypage.html"
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        
        # ログイン中のユーザーのIDを取得
        user_id = self.request.user.id
        
        # 現在の日付を取得
        current_date = datetime.date.today()
        
        # ログイン中のユーザーの過去の予約オブジェクトを取得
        past_bookings = Booking.objects.filter(user_id=user_id, booking_date__lt=current_date)
        
        # ログイン中のユーザーの将来の予約オブジェクトを取得
        future_bookings = Booking.objects.filter(user_id=user_id, booking_date__gte=current_date)
        
        # Favoriteオブジェクトを取得し、関連するRestaurantオブジェクトも同時に取得する
        favorites_with_restaurant = Favorite.objects.select_related('restaurant').filter(user_id=user_id)
        
        # コンテキストに過去の予約と新規予約を追加
        context['past_bookings'] = past_bookings
        context['future_bookings'] = future_bookings
        
        # modelで定義したレビューのオブジェクトを取得
        context['reviews'] = Review.objects.filter(user_id=user_id)
        
        # お気に入りのオブジェクトとそれに関連するRestaurantオブジェクトをコンテキストに追加
        context['favorites'] = favorites_with_restaurant
        
        context['user'] =self.request.user

        return context