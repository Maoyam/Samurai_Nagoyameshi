from django.shortcuts import render, redirect
from commondb.models.user import User
from django.views.generic.edit import UpdateView

class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', ]
    template_name = 'general/user_update.html'
    