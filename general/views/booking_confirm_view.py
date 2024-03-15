from django.views.generic import TemplateView
    
class BookingCompleteView(TemplateView):
    template_name = 'general/complete_booking.html'
