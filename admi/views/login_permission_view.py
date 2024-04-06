# from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import View


class AdmiRequiredView(UserPassesTestMixin, View):
    # パーミッションを指定
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_manage_member == True

    raise_exception = False
    login_url = reverse_lazy("admi:admi_login")
