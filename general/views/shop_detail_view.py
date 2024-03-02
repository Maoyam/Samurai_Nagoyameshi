from typing import Any
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView
from commondb.models.restaurant import Restaurant
from commondb.models.booking import Booking
from commondb.models.review import Review
from ..forms import BookingForm


class ShopDetailView(DetailView):
    model = Restaurant
    #詳細ページのテンプレート名
    template_name = 'general/shop_detail.html'
    # テンプレート内でのオブジェクトの名前
    context_object_name = 'restaurant'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            if self. request.user.is_paid_member:
                context['user_type'] = 'is_paid'
            else:
                context['user_type'] = 'member'
        else:
            context['user_type'] = 'no_member'
        return context
    

class BookingCreateView(CreateView):
    model = Booking
    template_name = 'general/shop_detail.html'
    form_class = BookingForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()  # フォームをコンテキストに追加
        return context


class ShopReviewView(TemplateView):
    template_name = 'general/shop_detail.html'
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        # URLから店舗のIDを取得
        restaurant_id = self.kwargs.get('pk')
        # 対象の店舗に関連するレビューを取得
        context['reviews'] = Review.objects.filter(restaurant_id=restaurant_id)
        return context
