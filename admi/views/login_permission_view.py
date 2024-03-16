from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import View


class AdmiRequiredView(PermissionRequiredMixin, View):
    # パーミッションを指定
    permission_required = 'admi.can_access_admin_view'
