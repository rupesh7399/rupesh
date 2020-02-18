from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model
from django.views.generic import CreateView, FormView
from .forms import *
from django.utils.http import is_safe_url


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
        email  = form.cleaned_data.get("email")
        password  = form.cleaned_data.get("password")
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