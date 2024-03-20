from typing import Any
import datetime
from commondb.models.booking import Booking
from commondb.models.review import Review
from commondb.models.favorite import Favorite
from commondb.models.user import User
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy

class MypageView(LoginRequiredMixin, TemplateView):
    template_name = "general/mypage.html"
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        
        # ログイン中のユーザーのIDを取得
        user_id = self.request.user.id
        
        mypage_id = kwargs.get('pk')
        # ログイン中のユーザーのIDとマイページのPKが一致しない場合はエラーを返す
        if user_id != mypage_id:
            raise PermissionDenied("このページの閲覧権限がありません")
        
        # 現在の日付を取得
        current_date = datetime.date.today()
        
        # ログイン中のユーザーの過去の予約オブジェクトを取得
        past_bookings = Booking.objects.filter(user_id=user_id, booking_date__lt=current_date).order_by('booking_date')
        
        # ログイン中のユーザーの将来の予約オブジェクトを取得
        future_bookings = Booking.objects.filter(user_id=user_id, booking_date__gte=current_date).order_by('booking_date')
        
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
    
class MypageBookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'general/booking_confirm_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('mypage', kwargs={'pk': self.request.user.id})
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        
        user_id = self.request.user.id
        context['user_id'] = user_id
        #確認表示用の予約情報
        booking = self.object
        context['booking_date'] = booking.booking_date
        context['booking_time'] = booking.booking_time
        context['numbers_of_ppl'] = booking.numbers_of_ppl
        context['restaurant_name'] = booking.restaurant.name
        return context
        
class MypageReviewDetailView(LoginRequiredMixin, DetailView):
    model = Review
    template_name = 'general/user_review_detail.html'
    context_object_name = 'review'
        
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        
        user_id = self.request.user.id
        context['user_id'] = user_id
        review_id = self.kwargs.get('pk')
        context['review_id'] = review_id
        return context   