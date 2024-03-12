from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import View


class AdmiRequiredMixin(PermissionRequiredMixin):
    # パーミッションを指定
    permission_required = 'admi.can_access_admin_view'

    login_url = 'admi:admi_login' 


class AdmiView(AdmiRequiredMixin, View):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            return reverse_lazy('admi:shop_list')  
        else:
            return reverse_lazy('admi:admi_login')
