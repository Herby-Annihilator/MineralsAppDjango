from django.shortcuts import render


# Create your views here.
from mineralsApp.models import *


def load_minerals_page(request):
    minerals = Mineral.objects.all()
    return render(request, 'admin.html', {'minerals': minerals})


def load_index_page(request):
    return render(request, 'index.html')

