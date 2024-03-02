from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'general/login.html'