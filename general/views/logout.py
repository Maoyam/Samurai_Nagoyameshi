from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'general/index.html/'