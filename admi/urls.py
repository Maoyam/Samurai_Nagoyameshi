from django.urls import path

from .views.company_views import CompanyUpdateView

app_name = 'admi'
urlpatterns = [
    path('company/<int:pk>/', CompanyUpdateView.as_view(), name="company_update"),
]
