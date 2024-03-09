from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView
from commondb.models.user import User

class AdmiUserListView(ListView):
    model = User
    template_name = 'admi/user_list.html'
    paginate_by = 10
    
class AdmiUserUpdateView(UpdateView):
    model = User
    template_name = 'admi/edit_user.html'
    fields = ['username', 'email', 'is_paid_member']
    success_url = reverse_lazy('admi:user_list')
    
class AdmiUserDeleteView(DeleteView):
    model = User
    template_name = 'admi/user_confirm_delete.html'
    success_url = reverse_lazy('admi:user_list')