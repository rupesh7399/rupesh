from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView, FormView, ListView, UpdateView
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Task
from accounts.models import User
from django.contrib import messages
import datetime


class DeshView(TemplateView):
    template_name = "desbord.html"


class createTask(FormView):
    form_class = CreateTask
    template_name = 'create.html'

    def form_valid(self, form):
        qs = User.objects.get(id=int(self.request.session["u_id"]))
        
        obj = Task()
        obj.user = qs
        obj.title = form.cleaned_data['title']
        obj.description = form.cleaned_data['description']
        obj.lastDate = form.cleaned_data['lastdate']
        obj.save()
        messages.success(self.request, 'Task is created!!.')
        for email in form.cleaned_data["Inspect"]:
            obj.Inspect.add(email)

        return super(createTask, self).form_invalid(form)

class TaskListView(ListView):
    model = Task
    template_name = 'list.html'
    def get_queryset(self):
        qs = User.objects.get(id=int(self.request.session["u_id"]))
        return Task.objects.filter(user=qs)

class TaskUpdate(View):
    template_name = 'list.html'
    def post(self,request):
        Task_id = int(request.POST.get('task_id'))
        st = Task.objects.get(id = Task_id)
        t1 = datetime.datetime.now()
        if Task_id is not None and st.startTime is None:
            a = Task.objects.filter(id = Task_id).update(startTime = t1)
            return redirect('List')
        else:
            
            a = Task.objects.filter(id = Task_id).update(endTime = t1)
            return redirect('List')


