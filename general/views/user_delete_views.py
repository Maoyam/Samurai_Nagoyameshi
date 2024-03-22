from django.urls import reverse_lazy
from django.views.generic.edit import  DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from commondb.models.user import User
    
class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'general/user_confirm_delete.html'
    success_url = reverse_lazy('top')
    
    def get_object(self, queryset=None):
        # ログイン中のユーザーを取得して返す
        return self.request.user

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # 必要に応じて追加のコンテキストデータを提供する
    #     return context