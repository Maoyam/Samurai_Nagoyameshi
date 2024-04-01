from django.contrib import admin
from .models.area import Area
from .models.genre import Genre
from .models.restaurant import Restaurant
from .models.review import Review
from .models.booking import Booking
from .models.favorite import Favorite
from .models.company import Company
from .models.reguration import Reguration
from .models.sale import Sale
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model


# ユーザー管理
User = get_user_model()

# 会社概要
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'established_date', 'capital', 'number_of_staff')

# 会員規約
class RegurationAdmin(admin.ModelAdmin):
    list_display = ('name','text')

#エリア 
class AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

# ジャンル
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview') # 管理画面で表示するフィールド

    def image_preview(self, obj):
        if obj.image:
            return mark_safe('<img src="{}" width="100" />'.format(obj.image.url))
        else:
            return 'No Image'
    image_preview.short_description = 'Image Preview' 

# 店舗   
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'name_alphabet', 'genre', 'address', 'area', 'phone', 'time', 'price_low', 'price_high', 'information', 'image')

# レビュー
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'user', 'visit_date', 'rating', 'comment', 'image1', 'image2', 'image3')
    
# 予約
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'user', 'booking_date', 'booking_time', 'numbers_of_ppl', 'create_date')
    
# お気に入り
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'user', 'create_date')

# 売り上げ
class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'month', 'total_sales', 'paid_member_count')
    
admin.site.register(User)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Reguration, RegurationAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Sale, SaleAdmin)