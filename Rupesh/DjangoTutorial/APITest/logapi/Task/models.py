from django.db import models
from django.conf import settings
from django.urls import reverse
User = settings.AUTH_USER_MODEL


class TaskManager(models.Manager):
    
    def new_or_get(self, request):
        task_id = request.session.get("task_id", None)
        qs = self.get_queryset().filter(id=task_id)
        if qs.count() == 1:
            new_obj = False
            task_obj = qs.first()
            if request.user.is_authenticated and task_obj.user is None:
                task_obj.user = request.user
                task_obj.save()
        else:
            task_obj = Task.objects.new(user=request.user)
            new_obj = True
            request.session['task_id'] = task_obj.id
        return task_obj, new_obj


class Task(models.Model):
    user = models.ForeignKey(User, related_name='fuser',
                             on_delete=models.CASCADE)
    Inspect = models.ManyToManyField(
        User, related_name='Inspect', blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=300)
    lastDate = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = TaskManager()

    # def __str__(self):
    #     return self.title

    # def get_absolute_url(self):
    #     return reverse('Task-detail', kwargs={'pk': self.pk})


class StatusS(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE)
    start = models.BooleanField(default=False)
    stime = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    


class StatusE(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE)
    end = models.BooleanField(default=False)
    etime = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    