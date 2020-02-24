from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from django.conf import settings
from django.urls import reverse
User = settings.AUTH_USER_MODEL



class TaskManager(models.Manager):
    def all(self):
        return super().get_queryset()
    def save(self,qs,form):
        obj = Task()
        obj.user = qs
        obj.title = form.cleaned_data['title']
        obj.description = form.cleaned_data['description']
        obj.lastDate = form.cleaned_data['lastdate']
        obj.save()
        for email in form.cleaned_data["Inspect"]:
            obj.Inspect.add(email)
         
    

class Task(models.Model):
    user = models.ForeignKey(User, related_name='user',
                             on_delete=models.CASCADE)
    Inspect = models.ManyToManyField(
        User, related_name='Inspect', blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=300)
    lastDate = models.DateField()
    startTime = models.DateTimeField(auto_now_add=False,null = True, blank=True, auto_now=False)
    endTime = models.DateTimeField(auto_now_add=False,null=True,blank=True,auto_now=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = TaskManager()
