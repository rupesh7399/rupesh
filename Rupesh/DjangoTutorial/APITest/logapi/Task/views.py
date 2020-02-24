from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, CreateView, FormView, ListView, UpdateView,DeleteView
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, Http404
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
        Task.objects.save(qs,form)
        
        messages.success(self.request, 'Task is created!!.')
        return redirect('List')


class TaskListView(View):
    template_name = 'list.html'

    def get(self, request, pk=None):
        if pk:
            task = Task.objects.get(id=pk)
            context = {
                "task": task,
            }
        # template_name = 'details.html'
            return render(request, 'details.html', context)
        else:
            qs = User.objects.get(id=int(request.session["u_id"]))
            user = Task.objects.filter(user=qs)
            watcher = Task.objects.filter(Inspect=qs)
            context = {
                "user": user,
                "watcher": watcher
            }
            return render(request, self.template_name, context)


class TaskUpdate(View):
    template_name = 'list.html'

    def post(self, request):
        Task_id = int(request.POST.get('task_id'))
        st = Task.objects.get(id=Task_id)
        t1 = datetime.datetime.now()
        if Task_id is not None and st.startTime is None:
            a = Task.objects.filter(id=Task_id).update(startTime=t1)
            return redirect('List')
        else:

            a = Task.objects.filter(id=Task_id).update(endTime=t1)
            return redirect('List')


class UpdateTaskView(UpdateView):
    model = Task
    fields = ['title', 'description', 'lastDate', 'Inspect']
    template_name = 'edit.html'
    success_url = '/Task/List'


class TaskDelete(DeleteView):
    model = Task
    template_name = 'delete_view.html'
    success_url = '/Task/List'
