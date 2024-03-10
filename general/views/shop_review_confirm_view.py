# from django.urls import reverse_lazy
# from django.views.generic import FormView, TemplateView
# from commondb.models.restaurant import Restaurant
# from ..forms import BookingForm

# class BookingConfirmationView(FormView):
#     template_name = 'general/confirm_booking.html'
#     form_class = BookingForm
#     success_url = reverse_lazy('confirm_complete')

#     def get_initial(self):
#         restaurant_id = self.kwargs.get('restaurant_id')  # URLからrestaurant_idを取得
#         restaurant = Restaurant.objects.get(pk=restaurant_id)
#         return {'restaurant': restaurant}

#     def form_valid(self, form):
#         # フォームが有効な場合に確認画面を表示
#         return super().form_valid(form)