from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('List', ProductListView.as_view(), name="product"),
    path('Detail/<int:pk>', ProductDetailView.as_view(), name="Detail"),
    path('Detail/<slug:slug>', ProductSlugView.as_view(), name="SlugDetail"),

]
