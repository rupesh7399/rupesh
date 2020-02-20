from django.contrib import admin
from django.urls import path, include
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user',views.UrgView)

urlpatterns = [
     path('register', views.RegisterView.as_view(), name='register'),
     path('', views.LoginView.as_view(), name="login"),
     path('user',include(router.urls)),
     # path('api-auth',include('rest_framework.urls')),
     path('api-token-auth/', views.CustomAuthToken.as_view()),

]
