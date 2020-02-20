from django.db import models
from accounts.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #Inspect = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=300)
    lastDate = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class StatusS(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE)
    start = models.BooleanField(default=False)
    stime = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)



class StatusE(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE)
    end  = models.BooleanField(default=False)
    etime = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
