from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from mineralsApp.forms import *


def load_minerals_page(request):
    minerals = Mineral.objects.all()
    return render(request, 'admin.html', {'minerals': minerals})


def load_index_page(request):
    return render(request, 'index.html')


def load_details_page(request, mineral_id):
    try:
        mineral = Mineral.objects.get(pk=mineral_id)
    except Mineral.DoesNotExist:
        raise Http404("Mineral does not exist")
    return render(request, 'minerals.html', {'mineral': mineral})


def load_edit_page(request, mineral_id):
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            form.save()

        mineral = Mineral.objects.get(pk=mineral_id)
        form = EditForm()
        return render(request, 'edit.html', {'mineral': mineral, 'form': form})


def load_create_page(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()

    form = CreateForm()
    return render(request, 'edit.html', {'form': form})


def delete_mineral(request, mineral_id):
    try:
        mineral = Mineral.objects.get(pk=mineral_id)
        mineral.delete()
    except Mineral.DoesNotExist:
        raise Http404("Mineral does not exist")
    return redirect('admin')
