from django.shortcuts import render
# PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteViewを追加
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

# class index(LoginRequiredMixin, generic.TemplateView):
#     """メニュービュー"""
#     template_name = 'accounts/top.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs) # 継承元のメソッドCALL
#         context["form_name"] = "top"
#         return context


class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    """パスワード変更ビュー"""
    success_url = reverse_lazy('password_change_done')
    template_name = 'general/password_change.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # 継承元のメソッドCALL
        context["form_name"] = "password_change"
        return context


class PasswordChangeDone(LoginRequiredMixin,PasswordChangeDoneView):
    """パスワード変更しました"""
    template_name = 'general/password_change_done.html'

# --- ここから追加
class PasswordReset(PasswordResetView):
    """パスワード変更用URLの送付ページ"""
    subject_template_name = 'general/mail_template/reset/subject.txt'
    email_template_name = 'general/mail_template/reset/message.txt'
    template_name = 'general/password_reset_form.html'
    success_url = reverse_lazy('password_reset_done')


class PasswordResetDone(PasswordResetDoneView):
    """パスワード変更用URLを送りましたページ"""
    template_name = 'general/password_reset_done.html'


class PasswordResetConfirm(PasswordResetConfirmView):
    """新パスワード入力ページ"""
    success_url = reverse_lazy('password_reset_complete')
    template_name = 'general/password_reset_confirm.html'


class PasswordResetComplete(PasswordResetCompleteView):
    """新パスワード設定しましたページ"""
    template_name = 'general/password_reset_complete.html'

# --- ここまで

