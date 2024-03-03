from typing import Any
from django.views.generic import TemplateView
from commondb.models.restaurant import Restaurant
from commondb.models.booking import Booking
from commondb.models.review import Review
from ..forms import BookingForm


class ShopTemplatelView(TemplateView):
    model = Restaurant
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
        
        #店舗詳細
        context['restaurant'] = Restaurant.objects.get(pk=restaurant_id)
            
        # レビュー
        # 対象の店舗に関連するレビューを取得
        context['reviews'] = Review.objects.filter(restaurant_id=restaurant_id)
        
        # 予約フォーム
        restaurant_ = Restaurant.objects.get(pk=restaurant_id)
        form = BookingForm(initial={'restaurant': restaurant_})
        context['form'] = form
        return context