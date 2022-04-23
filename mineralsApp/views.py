from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from mineralsApp.models import *


def load_minerals_page(request):
    minerals = Mineral.objects.all()
    return render(request, 'admin.html', {'minerals': minerals})


def load_index_page(request):
    return render(request, 'index.html')


def load_details_page(request, mineral_id):
    try:
        mineral = Mineral.objects.get(pk=mineral_id)
    except Mineral.DoesNotExist:
        raise Http404("Mineral does not exists")
    return render(request, 'minerals.html', {'mineral': mineral})


def load_edit_page(request, mineral_id):
    try:
        mineral = Mineral.objects.get(pk=mineral_id)
    except Mineral.DoesNotExist:
        raise Http404("Mineral does not exists")
    return render(request, 'edit.html', {'mineral': mineral})


def delete_mineral(request, mineral_id):
    try:
        mineral = Mineral.objects.get(pk=mineral_id)
        mineral.delete()
    except Mineral.DoesNotExist:
        raise Http404("Mineral does not exists")
    return redirect('admin')



