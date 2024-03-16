from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from commondb.models.booking import Booking
from ..views.login_permission_view import AdmiRequiredView

class AdmiBookingListView(AdmiRequiredView, ListView):
    model = Booking
    template_name = 'admi/booking_list.html'
    paginate_by = 10

class AdmiBookingCreateView(AdmiRequiredView, CreateView):
    model = Booking
    template_name = 'admi/add_booking.html'
    fields = '__all__'
    success_url = reverse_lazy('admi:booking_list')
    
class AdmiBookingUpdateView(AdmiRequiredView, UpdateView):
    model = Booking
    template_name = 'admi/edit_booking.html'
    fields = '__all__'
    
class AdmiBookingDeleteView(AdmiRequiredView, DeleteView):
    model = Booking
    template_name = 'admi/booking_confirm_delete.html'
    success_url = reverse_lazy('admi:booking_list')
    
class AdmiBookingDetailView(AdmiRequiredView, DetailView):
    model = Booking
    template_name = 'admi/booking_detail.html'
    context_object_name = 'booking'