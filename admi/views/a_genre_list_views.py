from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from commondb.models.genre import Genre
from ..views.login_permission_view import AdmiRequiredView

class AdmiGenreListView(AdmiRequiredView, ListView):
    model = Genre
    template_name = 'admi/genre_list.html'
    paginate_by = 10
    
    pass

class AdmiGenreCreateView(AdmiRequiredView, CreateView):
    model = Genre
    template_name = 'admi/add_genre.html'
    fields = '__all__'
    success_url = reverse_lazy('admi:genre_list')
    
class AdmiGenreUpdateView(AdmiRequiredView, UpdateView):
    model = Genre
    template_name = 'admi/edit_genre.html'
    fields = '__all__'
    
class AdmiGenreDeleteView(AdmiRequiredView, DeleteView):
    model = Genre
    template_name = 'admi/genre_confirm_delete.html'
    success_url = reverse_lazy('admi:genre_list')
    