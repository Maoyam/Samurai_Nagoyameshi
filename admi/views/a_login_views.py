from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib import messages

class LoginView(LoginView):
     form_class = AuthenticationForm
     template_name = 'admi/login.html'
     
class LogoutView(LoginRequiredMixin, LogoutView):
     next_page = reverse_lazy('admi:admi_login')

        
