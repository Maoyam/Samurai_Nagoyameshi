from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from ..forms import UserRegistrationForm

class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'general/user_form.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # ユーザーを認証してログインする
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)            
            return redirect('top')  # 登録成功後のリダイレクト先を指定
        return render(request, 'general/user_form.html', {'form': form})