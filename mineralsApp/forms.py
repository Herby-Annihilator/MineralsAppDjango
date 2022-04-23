from django import forms
from mineralsApp.models import *


class EditForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=1024)
    researchers = forms.CharField(max_length=1024)
    publications = forms.CharField(max_length=1024)
    territories = forms.CharField(max_length=1024)
    fields = forms.CharField(max_length=1024)


class CreateForm(forms.ModelForm):
    class Meta:
        model = Mineral
        fields = ['name', 'description']
