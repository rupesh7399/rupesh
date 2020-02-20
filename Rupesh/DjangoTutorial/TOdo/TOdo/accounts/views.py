from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model
from django.views.generic import CreateView, FormView
from .forms import *
from django.utils.http import is_safe_url
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken

# API REGISTER


class CustomAuthToken(APIView):

    def post(self, request, *args, **kwargs):
        response_data = {}
        request = self.request
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            response_data["message"] = "Success"
            response_data["status"] = True
            response_data["data"] = {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }
        else:
            refresh = RefreshToken.for_user(user)
            response_data["message"] = " not provided."
            response_data["status"] = False
            response_data["data"] = {
                
            }


class UrgView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = 'login'


class LoginView(FormView):
    form_class = LoginForm
    success_url = 'admin'
    template_name = 'login.html'

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
            try:
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        return super(LoginView, self).form_invalid(form)
