from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views import View
from commondb.models.restaurant import Restaurant
from django.db.models import Q, Avg
from commondb.models.review import Review
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



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

            
        paginator = Paginator(restaurants, 12)  # 1ページに12個の店舗を表示

        page_number = request.GET.get('page')
        try:
            restaurants = paginator.page(page_number)
        except PageNotAnInteger:
            # ページ番号が整数でない場合は、最初のページを表示
            restaurants = paginator.page(1)
        except EmptyPage:
            # ページ番号が範囲外の場合は、最後のページを表示
            restaurants = paginator.page(paginator.num_pages)
        
        return render(request, 'general/shop_list_search.html', {'restaurants': restaurants, 'keyword': keyword})

class GenreFilterView(View):
    def get(self, request, genre):
        restaurants = Restaurant.objects.filter(genre=genre)  # ジャンルに一致する店舗を検索
        paginator = Paginator(restaurants, 12)  # 1ページに12個の店舗を表示

        page_number = request.GET.get('page')
        try:
            restaurants = paginator.page(page_number)
        except PageNotAnInteger:
            # ページ番号が整数でない場合は、最初のページを表示
            restaurants = paginator.page(1)
        except EmptyPage:
            # ページ番号が範囲外の場合は、最後のページを表示
            restaurants = paginator.page(paginator.num_pages)
        
        return render(request, 'general/shop_list_filter.html', {'restaurants': restaurants})

class AreaFilterView(View):
    def get(self, request, area):

        restaurants = Restaurant.objects.filter(area=area)  # エリアに一致する店舗を検索
        
        paginator = Paginator(restaurants, 12)  # 1ページに12個の店舗を表示

        page_number = request.GET.get('page')
        try:
            restaurants = paginator.page(page_number)
        except PageNotAnInteger:
            # ページ番号が整数でない場合は、最初のページを表示
            restaurants = paginator.page(1)
        except EmptyPage:
            # ページ番号が範囲外の場合は、最後のページを表示
            restaurants = paginator.page(paginator.num_pages)
            
        return render(request, 'general/shop_list_filter.html', {'restaurants': restaurants})
    
