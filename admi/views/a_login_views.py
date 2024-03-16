from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.shortcuts import redirect

class AdmiLoginView(LoginView):
     form_class = AuthenticationForm
     template_name = 'admi/login.html'
     success_url = reverse_lazy('admi:shop_list')
     
     def get_success_url(self):
          return reverse_lazy('admi:shop_list')
     
     def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            # ログイン済みのユーザーはshop_listにリダイレクト
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)
     
class AdmiLogoutView(LoginRequiredMixin, LogoutView):
     next_page = reverse_lazy('admi:admi_login')
