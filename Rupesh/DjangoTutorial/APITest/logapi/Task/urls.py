from django.contrib import admin
from django.urls import path, include
from .import views

from rest_framework import routers
router = routers.DefaultRouter()


urlpatterns = [
    path('des',views.DeshView.as_view()),
    path('create',views.createTask.as_view(),name='create'),
    path('List',views.TaskListView.as_view(),name="List"),
    path('start-end',views.TaskUpdate.as_view(),name="start-end"),
    path('update/<int:pk>',views.UpdateTaskView.as_view(),name="update"),
    path('Details/<int:pk>',views.TaskListView.as_view(),name="Details"),
    path('<int:pk>/delete',views.TaskDelete.as_view(),name="delete"),

]
