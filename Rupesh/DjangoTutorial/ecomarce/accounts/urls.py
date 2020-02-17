from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import logout

urlpatterns = [
    path('login/',views.LoginView.as_view(),name="login"),
    path(' Register',views.RegisterView.as_view(),name="reg"),
    path('logout',views.logout,name="logout"),
    path('guest_register',views.guest_register_view, name="guest_register"),
]
