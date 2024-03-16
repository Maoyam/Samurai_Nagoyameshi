from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from commondb.models.restaurant import Restaurant
from ..views.login_permission_view import AdmiRequiredView

class AdmiShopListView(AdmiRequiredView, ListView):
    model = Restaurant
    template_name = 'admi/shop_list.html'
    paginate_by = 10

class AdmiShopCreateView(AdmiRequiredView, CreateView):
    model = Restaurant
    template_name = 'admi/add_shop.html'
    fields = '__all__'
    success_url = reverse_lazy('admi:shop_list')
    
class AdmiShopUpdateView(AdmiRequiredView, UpdateView):
    model = Restaurant
    template_name = 'admi/edit_shop.html'
    fields = '__all__'
    
class AdmiShopDeleteView(AdmiRequiredView, DeleteView):
    model = Restaurant
    template_name = 'admi/shop_confirm_delete.html'
    success_url = reverse_lazy('admi:shop_list')
    
class AdmiShopDetailView(AdmiRequiredView, DetailView):
    model = Restaurant
    template_name = 'admi/shop_detail.html'
    context_object_name = 'restaurant'