from django.urls import path
from .views.company_views import CompanyUpdateView
from .views.a_shop_list_views import AdmiShopListView, AdmiShopCreateView, AdmiShopUpdateView, AdmiShopDeleteView, AdmiShopDetailView
from .views.a_user_list_views import AdmiUserDeleteView, AdmiUserListView, AdmiUserUpdateView
from .views.a_reguration_views import RegTemplateView, RegUpdateView

app_name = 'admi'
urlpatterns = [
    path('company/<int:pk>/', CompanyUpdateView.as_view(), name="company_update"),
    path('shop_list/', AdmiShopListView.as_view(), name="shop_list"),
    path('add_shop/', AdmiShopCreateView.as_view(), name="add_shop"),
    path('edit_shop/<int:pk>/', AdmiShopUpdateView.as_view(), name="edit_shop"),
    path('delete_shop/<int:pk>', AdmiShopDeleteView.as_view(), name="delete_shop"),
    path('shop_detail/<int:pk>', AdmiShopDetailView.as_view(), name="shop_detail"),
    path('user_list/', AdmiUserListView.as_view(), name="user_list"),
    path('edit_user/<int:pk>/', AdmiUserUpdateView.as_view(), name="edit_user"),
    path('delete_user/<int:pk>', AdmiUserDeleteView.as_view(), name="delete_user"),
    path('reguration/', RegTemplateView.as_view(), name="reguration"),
    path('edit_reguration/<int:pk>', RegUpdateView.as_view(), name="edit_reguration"),   
]
