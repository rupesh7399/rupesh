from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('task',views.TaskView)

urlpatterns = [
    path('t1',include(router.urls))
]
