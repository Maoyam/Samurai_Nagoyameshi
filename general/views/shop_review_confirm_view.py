from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from commondb.models.restaurant import Restaurant
from commondb.models.booking import Booking

class BookingConfirmationView(TemplateView):
    template_name = 'general/confirm_booking.html'

    def post(self, request, *args, **kwargs):
        # POSTデータから予約情報を取得
        restaurant_id = request.POST.get('restaurant_id')
        booking_date = request.POST.get('booking_date')
        booking_time = request.POST.get('booking_time')
        numbers_of_ppl = request.POST.get('numbers_of_ppl')
        
        # 予約を作成
        restaurant = Restaurant.objects.get(pk=restaurant_id)
        booking = Booking.objects.create(
            restaurant=restaurant,
            booking_date=booking_date,
            booking_time=booking_time,
            numbers_of_ppl=numbers_of_ppl
        )
        
        # 予約完了ページにリダイレクト
        return HttpResponseRedirect('/general/booking_complete/')
    
class BookingCompleteView(TemplateView):
    template_name = 'general/confirm_complete.html'