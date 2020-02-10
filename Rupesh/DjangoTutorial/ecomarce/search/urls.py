from django.contrib import admin
from django.urls import path, include
from products.views import  ProductListView
from .views import *

app_name = 'search'
urlpatterns = [
    path('', SearchProductListView.as_view(), name="search"),
    

]
