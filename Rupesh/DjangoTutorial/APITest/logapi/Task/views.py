from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView, FormView
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class DeshView(TemplateView):
    template_name = "desbord.html"
    


class createTask(FormView):
    form_class = CreateTask
    #initial = {'id': 'value'}
    template_name = 'create.html'
    
    def form_valid(self,form):
        create = CreateTask()
        #qs = User.objects.get(id = int(self.request.session[2]))
        create.user = 1
        create.title = form.cleaned_data.get("title")
        create.description = form.cleaned_data.get("description")
        create.lastdate = form.cleaned_data.get("lastdate")
        create.Inspect = form.cleaned_data.get("Inspect")
        create.save()
        
        return super(createTask, self).form_invalid(form)
    
    

    