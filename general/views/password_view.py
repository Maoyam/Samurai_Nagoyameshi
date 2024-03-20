from django.shortcuts import render
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy




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

# # --- ここから追加
# class PasswordReset(PasswordResetView):
#     email_template_name = 'general/password_reset_email.html'
#     extra_email_context = None
#     form_class = PasswordResetForm
#     from_email = None
#     html_email_template_name = None
#     subject_template_name = 'general/password_reset_subject.txt'
#     success_url = reverse_lazy('password_reset_done')
#     template_name = 'registration/password_reset_form.html'
#     title = _('Password reset')
#     token_generator = default_token_generator



# class PasswordResetDone(PasswordResetDoneView):
#     """パスワード変更用URLを送りましたページ"""
#     template_name = 'general/password_reset_done.html'


# class PasswordResetConfirm(PasswordResetConfirmView):
#     """新パスワード入力ページ"""
#     success_url = reverse_lazy('password_reset_complete')
#     template_name = 'general/password_reset_confirm.html'
#     post_reset_login = True


# class PasswordResetComplete(PasswordResetCompleteView):
#     """新パスワード設定しましたページ"""
#     template_name = 'general/password_reset_complete.html'

# # --- ここまで

