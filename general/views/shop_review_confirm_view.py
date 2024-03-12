from django.views.generic import TemplateView
from django.shortcuts import redirect
from commondb.models.booking import Booking

class BookingConfirmationView(TemplateView):
    template_name = 'general/confirm_booking.html'

    def post(self, request, *args, **kwargs):
        # 予約フォームのデータを取得
        booking_data = {
            'booking_date': request.POST.get('booking_date'),
            'booking_time': request.POST.get('booking_time'),
            'numbers_of_ppl': request.POST.get('numbers_of_ppl'),
        }
        # 予約を作成
        booking = Booking.objects.create(**booking_data)
        # 予約の確定後、適切なページにリダイレクト
        return redirect('booking_confirmed', pk=booking.pk)
