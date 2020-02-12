from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import logout

urlpatterns = [
    path('login/',views.login_page,name="login"),
    path(' Register',views.register_page,name="reg"),
    path('logout',views.logout,name="logout"),
    path('guest_register',views.guest_register_view, name="guest_register"),
]
