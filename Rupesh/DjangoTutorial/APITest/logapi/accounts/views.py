from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model
from django.views.generic import CreateView, FormView
from .forms import *
from django.utils.http import is_safe_url
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User, auth


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = '/'


class LoginView(FormView):
    form_class = LoginForm
    success_url = 'admin'
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('Task/des')
        return super(LoginView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        request = self.request
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            request.session['email'] = user.id
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        return super(LoginView, self).form_invalid(form)


def logout(request):
    auth.logout(request)
    return redirect('/')
