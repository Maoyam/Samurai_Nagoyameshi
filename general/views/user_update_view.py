from django.shortcuts import render, redirect
from commondb.models.user import User
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', ]
    template_name = 'general/user_update.html'
    