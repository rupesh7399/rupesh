from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from django.conf import settings
from django.urls import reverse
User = settings.AUTH_USER_MODEL




    

class Task(models.Model):
    user = models.ForeignKey(User, related_name='fuser',
                             on_delete=models.CASCADE)
    Inspect = models.ManyToManyField(
        User, related_name='Inspect', blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=300)
    lastDate = models.DateField()
    startTime = models.DateTimeField(auto_now_add=False,null = True, blank=True, auto_now=False)
    endTime = models.DateTimeField(auto_now_add=False,null=True,blank=True,auto_now=False)
    timestamp = models.DateTimeField(auto_now_add=True)


