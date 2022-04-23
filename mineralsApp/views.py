from django.shortcuts import render
from models import *


# Create your views here.


def load_minerals_page(request):
    minerals = Mineral.objects.all()
    return render(request, 'admin.html', {'minerals': minerals})


def load_index_page(request):
    return render(request, 'index.html')

