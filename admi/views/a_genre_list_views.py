from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from commondb.models.genre import Genre

class AdmiGenreListView(ListView):
    model = Genre
    template_name = 'admi/genre_list.html'
    paginate_by = 10

class AdmiGenreCreateView(CreateView):
    model = Genre
    template_name = 'admi/add_genre.html'
    fields = '__all__'
    success_url = reverse_lazy('admi:genre_list')
    
class AdmiGenreUpdateView(UpdateView):
    model = Genre
    template_name = 'admi/edit_genre.html'
    fields = '__all__'
    
class AdmiGenreDeleteView(DeleteView):
    model = Genre
    template_name = 'admi/genre_confirm_delete.html'
    success_url = reverse_lazy('admi:genre_list')
    