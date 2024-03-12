from django.urls import path
from .views.company_views import CompanyUpdateView
from .views.a_shop_list_views import AdmiShopListView, AdmiShopCreateView, AdmiShopUpdateView, AdmiShopDeleteView, AdmiShopDetailView
from .views.a_user_list_views import AdmiUserDeleteView, AdmiUserListView, AdmiUserUpdateView
from .views.a_reguration_views import RegTemplateView, RegUpdateView
from .views.a_genre_list_views import AdmiGenreListView, AdmiGenreCreateView, AdmiGenreUpdateView, AdmiGenreDeleteView
from .views.a_booking_list_views import AdmiBookingListView, AdmiBookingDetailView, AdmiBookingUpdateView, AdmiBookingDeleteView
from .views.a_login_views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'admi'
urlpatterns = [
    path('login/', LoginView.as_view(), name="admi_login"),
    path('logout/', LogoutView.as_view(), name="admi_logout"),
    path('company/<int:pk>/', CompanyUpdateView.as_view(), name="company_update"),
    path('shop_list/', AdmiShopListView.as_view(), name="shop_list"),
    path('add_shop/', AdmiShopCreateView.as_view(), name="add_shop"),
    path('edit_shop/<int:pk>/', AdmiShopUpdateView.as_view(), name="edit_shop"),
    path('delete_shop/<int:pk>/', AdmiShopDeleteView.as_view(), name="delete_shop"),
    path('shop_detail/<int:pk>/', AdmiShopDetailView.as_view(), name="shop_detail"),
    path('user_list/', AdmiUserListView.as_view(), name="user_list"),
    path('edit_user/<int:pk>/', AdmiUserUpdateView.as_view(), name="edit_user"),
    path('delete_user/<int:pk>/', AdmiUserDeleteView.as_view(), name="delete_user"),
    path('reguration/', RegTemplateView.as_view(), name="reguration"),
    path('edit_reguration/<int:pk>', RegUpdateView.as_view(), name="edit_reguration"),
    path('genre_list/', AdmiGenreListView.as_view(), name="genre_list"),
    path('add_genre/', AdmiGenreCreateView.as_view(), name="add_genre"),
    path('edit_genre/<int:pk>/', AdmiGenreUpdateView.as_view(), name="edit_genre"),
    path('delete_genre/<int:pk>/', AdmiGenreDeleteView.as_view(), name="delete_genre"),
    path('booking_list/', AdmiBookingListView.as_view(), name="booking_list"),
    path('edit_booking/<int:pk>/', AdmiBookingUpdateView.as_view(), name="edit_booking"),
    path('delete_booking/<int:pk>/', AdmiBookingDeleteView.as_view(), name="delete_booking"),
    path('booking_detail/<int:pk>/', AdmiBookingDetailView.as_view(), name="booking_detail"),
]   


# MEDIA_URL に対する URL パターンを追加します
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)