from django.shortcuts import redirect, get_object_or_404
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
        restaurant_ = Restaurant.objects.get(pk=restaurant_id)
        form = BookingForm(initial={'restaurant': restaurant_})  # フォームにrestaurant_idを初期値として設定
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        restaurant_id = self.kwargs.get('pk')
        form = BookingForm(request.POST)
        if form.is_valid():
        # フォームが有効な場合、確認ページにリダイレクトする
            return redirect(reverse('confirm_booking', kwargs={'pk': restaurant_id}))
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)
        
        # form = self.form_class(request.POST)
        # if form.is_valid():
        #     restaurant = form.cleaned_data['restaurant']
        #     # 予約フォームが有効な場合、確認ページにリダイレクトする
        #     return redirect(reverse('confirm_booking', kwargs={'restaurant_id': restaurant.id}))
        # else:
        #     context = self.get_context_data(**kwargs)
        #     context['form'] = form
        #     return self.render_to_response(context)