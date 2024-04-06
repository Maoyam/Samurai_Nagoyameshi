from django.contrib.auth.views import LoginView, LogoutView
from ..views.login_permission_view import AdmiRequiredView
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
          if self.request.user.is_authenticated and self.request.user.is_manage_member:

               return redirect(self.success_url)
          return super().dispatch(request, *args, **kwargs)
     
class AdmiLogoutView(AdmiRequiredView, LogoutView):
     next_page = reverse_lazy('admi:admi_login')
