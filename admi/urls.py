from django.urls import path

from .views.company_views import CompanyCreateView

app_name = 'admi'
urlpatterns = [
    path('company/', CompanyCreateView.as_view(), name="company_form"),
]
