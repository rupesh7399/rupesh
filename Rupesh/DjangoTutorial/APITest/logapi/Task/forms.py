from django import forms
from .models import *
from accounts.models import User


class CreateTask(forms.Form):
     
     title = forms.CharField(label='Title',required=True)
     description = forms.CharField(label='Description',widget=forms.Textarea,required=True)
     lastdate = forms.DateField( required=True,widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'type': 'date'
        }))
     Inspect = forms.ModelMultipleChoiceField(queryset=User.objects.all(),widget=forms.SelectMultiple(attrs={"class": "form-control",}))
     
