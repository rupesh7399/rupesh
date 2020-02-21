from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView, FormView, ListView
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import *
from accounts.models import User


class DeshView(TemplateView):
    template_name = "desbord.html"


class createTask(FormView):
    form_class = CreateTask
    template_name = 'create.html'

    def form_valid(self, form):
        qs = User.objects.get(id=int(self.request.session["u_id"]))
        print(qs)
        obj = Task()
        obj.user = qs
        obj.title = form.cleaned_data['title']
        obj.description = form.cleaned_data['description']
        obj.lastDate = form.cleaned_data['lastdate']
        obj.save()
        for email in form.cleaned_data["Inspect"]:
            obj.Inspect.add(email)

        return super(createTask, self).form_invalid(form)

class TaskListView(ListView):
    model = Task
    template_name = 'list.html'
    def get_queryset(self):
        qs = User.objects.get(id=int(self.request.session["u_id"]))
        return Task.objects.all().filter(user==qs)

    
