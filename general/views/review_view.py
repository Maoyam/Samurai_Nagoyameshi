from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from general.forms import ReviewForm
from commondb.models.restaurant import Restaurant
from django.http import HttpResponse

class SubmitReviewView(View):
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
        return render(request, 'general/submit_review.html', {'form': form, 'restaurant': restaurant})

class ReviewConfirmationView(View):
    def get(self, request):
        restaurant_id = request.session.get('restaurant_id')  # レビュー投稿で設定されたrestaurant_idをセッションから取得
        if not restaurant_id:
            # もしrestaurant_idがセッションにない場合は、適切なエラー処理を行うか、リダイレクトするなどの方法で対処する
            return HttpResponse("Error: restaurant_id is missing")
        return render(request, 'general/review_confirmation.html', {'restaurant_id': restaurant_id})
