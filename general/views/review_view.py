from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import UpdateView
from general.forms import ReviewForm
from commondb.models.restaurant import Restaurant
from general.forms import Review
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse

class SubmitReviewView(LoginRequiredMixin, View):
    def get(self, request, restaurant_id):
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
        form = ReviewForm()
        return render(request, 'general/submit_review.html', {'form': form, 'restaurant': restaurant})
    
    def post(self, request, restaurant_id):
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant = restaurant
            review.user = request.user
            review.save()
            
            request.session['restaurant_id'] = restaurant_id           
            return redirect('top')
        else:
            return render(request, 'general/submit_review.html', {'form': form, 'restaurant': restaurant})

class ReviewConfirmationView(LoginRequiredMixin, View):
    def get(self, request):
        restaurant_id = request.session.get('restaurant_id')  # レビュー投稿で設定されたrestaurant_idをセッションから取得
        if not restaurant_id:
            # もしrestaurant_idがセッションにない場合は、適切なエラー処理を行うか、リダイレクトするなどの方法で対処する
            return HttpResponse("Error: restaurant_id is missing")
        return render(request, 'general/review_confirmation.html', {'restaurant_id': restaurant_id})
    
class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    template_name = 'general/review_update.html'
    fields = ['rating', 'comment', 'image1', 'image2', 'image3']
    
    def form_valid(self, form):
        # フォームが有効な場合は保存する前に画像を処理する
        review = form.save(commit=False)
        # ログインユーザーを設定
        review.user = self.request.user  

        # 画像フィールドをチェックし、ファイルがアップロードされているか確認する
        if 'image1' in self.request.FILES:
            review.image1 = self.request.FILES['image1']
        if 'image2' in self.request.FILES:
            review.image2 = self.request.FILES['image2']
        if 'image3' in self.request.FILES:
            review.image3 = self.request.FILES['image3']

        # レビューを保存
        review.save()
        return HttpResponseRedirect(reverse('mypage_review_detail', kwargs={'pk': review.pk}))

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        
        review_id = self.kwargs.get('pk')
        context['review_id'] = review_id
        
        review = self.get_object()
        context['restaurant_name'] = review.restaurant.name
        
        return context   