from django.contrib import admin
from django.urls import path, include
from .import views

from rest_framework import routers
router = routers.DefaultRouter()


urlpatterns = [
    path('register', views.RegisterView.as_view(), name='register'),
    path('', views.LoginView.as_view(), name="login"),
    path('login', views.LoginView.as_view(), name="login"),
    path('logout',views.logout,name="logout"),
    
]
