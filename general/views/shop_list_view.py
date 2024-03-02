from django.shortcuts import render, get_object_or_404
from django.views import View
from commondb.models.restaurant import Restaurant
from django.db.models import Q

class SearchView(View):
    def get(self, request):
        keyword = request.GET.get('search')
        if keyword:
            
            # 検索キーワードを正規化
            
            restaurants = Restaurant.objects.filter(
                Q(name__icontains=keyword) |  # 名前がキーワードに一致するか
                Q(area__name__icontains=keyword) |  # エリアがキーワードに一致するか
                Q(genre__name__icontains=keyword)  # ジャンルがキーワードに一致するか
            )
        else:
            restaurants = Restaurant.objects.all()  # キーワードが指定されていない場合はすべての店舗を取得
        
        return render(request, 'general/shop_list_search.html', {'restaurants': restaurants, 'keyword': keyword})

class GenreFilterView(View):
    def get(self, request, genre):
        restaurants = Restaurant.objects.filter(genre=genre)  # ジャンルに一致する店舗を検索
        return render(request, 'general/shop_list_filter.html', {'restaurants': restaurants})

class AreaFilterView(View):
    def get(self, request, area):

        restaurants = Restaurant.objects.filter(area=area)  # エリアに一致する店舗を検索
        return render(request, 'general/shop_list_filter.html', {'restaurants': restaurants})
