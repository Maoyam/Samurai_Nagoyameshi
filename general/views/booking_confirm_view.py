from django.views.generic import TemplateView
from django.shortcuts import redirect
from commondb.models.booking import Booking
from ..forms import BookingForm
from django.shortcuts import get_object_or_404

class BookingConfirmationView(TemplateView):
    template_name = 'general/confirm_booking.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        booking_id = self.kwargs.get('pk')
        booking = get_object_or_404(Booking, pk=booking_id)
        context['booking'] = booking
        return context
    
    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            return redirect('complete_booking', pk=booking.pk)
        else:
            # フォームが無効な場合は適切な処理を行う
            pass

#     def post(self, request, *args, **kwargs):
#         # 予約フォームのデータを取得
#         booking_data = {
#             'booking_date': request.POST.get('booking_date'),
#             'booking_time': request.POST.get('booking_time'),
#             'numbers_of_ppl': request.POST.get('numbers_of_ppl'),
#         }
#         # 予約を作成
#         booking = Booking.objects.create(**booking_data)
#         # 予約の確定後、適切なページにリダイレクト
#         return redirect('complete_booking', pk=booking.pk)
    
# class BookingCompleteView(TemplateView):
#     template_name = 'general/complete_booking.html'
