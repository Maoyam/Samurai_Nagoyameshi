from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from commondb.models.restaurant import Restaurant
from commondb.models.review import Review
from ..forms import BookingForm


class ShopTemplatelView(CreateView):
    model = Restaurant
    #詳細ページのテンプレート名
    template_name = 'general/shop_detail.html'
    # 予約フォーム
    form_class = BookingForm
    success_url = reverse_lazy('confirm_booking')
    
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
        restaurant_instance = get_object_or_404(Restaurant, pk=restaurant_id)
        form = BookingForm(initial={'restaurant': restaurant_instance})  # フォームにrestaurant_idを初期値として設定
        context['form'] = form
        return context

    def form_valid(self, form):
        restaurant_id = self.kwargs.get('pk')
        form.instance.restaurant_id = restaurant_id
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

    def get_success_url(self):
        restaurant_id = self.kwargs.get('pk')
        return reverse('confirm_booking', kwargs={'pk': restaurant_id})
        
