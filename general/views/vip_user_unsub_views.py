from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from commondb.models.user import User

class VipUserUnsubView(LoginRequiredMixin, TemplateView):
    template_name = 'general/vip_user_confirm_unsub.html'
    model = User

    def post(self, request):
        # ログインユーザーの is_paid_user を False に変更
        request.user.is_paid_member = False
        request.user.save()
        return redirect('mypage', pk=request.user.pk)
