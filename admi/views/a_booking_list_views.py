from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from commondb.models.booking import Booking
from .login_permission_view import AdmiView

class AdmiBookingListView(AdmiView, ListView):
    model = Booking
    template_name = 'admi/booking_list.html'
    paginate_by = 10

class AdmiBookingCreateView(AdmiView, CreateView):
    model = Booking
    template_name = 'admi/add_booking.html'
    fields = '__all__'
    success_url = reverse_lazy('admi:booking_list')
    
class AdmiBookingUpdateView(AdmiView, UpdateView):
    model = Booking
    template_name = 'admi/edit_booking.html'
    fields = '__all__'
    
class AdmiBookingDeleteView(AdmiView, DeleteView):
    model = Booking
    template_name = 'admi/booking_confirm_delete.html'
    success_url = reverse_lazy('admi:booking_list')
    
class AdmiBookingDetailView(AdmiView, DetailView):
    model = Booking
    template_name = 'admi/booking_detail.html'
    context_object_name = 'booking'