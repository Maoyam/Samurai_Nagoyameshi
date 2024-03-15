from django.views.generic import TemplateView, FormView
from django.shortcuts import redirect
from commondb.models.booking import Booking
from ..forms import BookingForm
from django.shortcuts import get_object_or_404

# class BookingConfirmationView(FormView):
#     template_name = 'general/confirm_booking.html'
#     form_class = BookingForm

#     def form_valid(self, form):
#         booking = form.save(commit=False)
#         booking.save()
#         return redirect('complete_booking', pk=booking.pk)

class BookingConfirmationView(TemplateView):
    template_name = 'general/confirm_booking.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # フォームを初期化してコンテキストに追加
        context['form'] = BookingForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.save()
            return redirect('complete_booking', pk=booking.pk)
        else:
            # フォームが無効な場合は適切な処理を行う
            pass
    
class BookingCompleteView(TemplateView):
    template_name = 'general/complete_booking.html'
