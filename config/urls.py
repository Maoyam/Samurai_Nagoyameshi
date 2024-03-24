"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from general.views.top_view import TopView
from general.views.login import LoginView
from general.views.logout import LogoutView
from general.views.shop_detail_view import ShopTemplatelView, FavoriteToggleView
from general.views.booking_confirm_view import BookingCompleteView
from general.views.shop_list_view import SearchView, GenreFilterView, AreaFilterView
from general.views.review_view import SubmitReviewView, ReviewConfirmationView, ReviewUpdateView
from general.views.mypage_view import MypageView, MypageBookingDeleteView, MypageReviewDetailView
from general.views.user_update_view import UserUpdateView
from general.views.user_register_view import RegisterView
from general.views.company_view import CompanyDetailView
from general.views.reguration_views import RegTemplateView
from general.views.password_view import PasswordChange, PasswordChangeDone
from django.contrib.auth import views as auth_views
from general.views.user_delete_views import UserDeleteView
from general.views import checkout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admi/', include('admi.urls')),
    path('', TopView.as_view(), name="top"),
    path('general/login/', LoginView.as_view(), name="login"),
    path('general/logout/', LogoutView.as_view(), name="logout"),
    path('general/shop_detail/<int:pk>/', ShopTemplatelView.as_view(), name="shop_detail"),
    path('favorite_toggle/<int:pk>/', FavoriteToggleView.as_view(), name="favorite_toggle"),
    path('general/booking_complete/', BookingCompleteView.as_view(), name="complete_booking"),
    path('general/shop_list_search/', SearchView.as_view(), name="search"),
    path('general/filter/genre/<int:genre>/', GenreFilterView.as_view(), name="shop_list_genre"),
    path('general/filter/area/<int:area>/', AreaFilterView.as_view(), name="shop_list_area"),
    path('general/submit_review/<int:restaurant_id>/', SubmitReviewView.as_view(), name="submit_review"),
    path('general/review_confirmation/<int:restaurant_id>/', ReviewConfirmationView.as_view(), name="review_confirmation"), 
    path('general/mypage/<int:pk>/', MypageView.as_view(), name='mypage'),
    path('general/mypage_booking_delete/<int:pk>/',MypageBookingDeleteView.as_view(), name="mypage_booking_delete"),
    path('general/mypage_review_detail/<int:pk>/', MypageReviewDetailView.as_view(), name="mypage_review_detail"),
    path('general/review_update/<int:pk>/', ReviewUpdateView.as_view(), name="review_update"),
    path('general/register/', RegisterView.as_view(), name="register"),
    path('general/user_update/<int:pk>/', UserUpdateView.as_view(), name="user_update"),
    path('general/user_delete/<int:pk>/', UserDeleteView.as_view(), name="user_delete"),
    path('general/company/<int:pk>/', CompanyDetailView.as_view(), name="company"),
    path('general/reguration/', RegTemplateView.as_view(), name="reguration"),
    path('password_change/', PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDone.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'), 
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('payment_checkout/', checkout_view.create_checkout_session, name="payment_checkout"),
    path('payment_successful/', checkout_view.create_checkout_session, name="payment_successful"),
    path('payment_cancelled', checkout_view.create_checkout_session, name="payment_cancelled"),
    path('create-checkout-session', checkout_view.customer_portal, name="payment_checkout"),
    path('stripe_webhook', checkout_view.webhook, name="stripe_webhook"),
    
]

# MEDIA_URL に対する URL パターンを追加
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
