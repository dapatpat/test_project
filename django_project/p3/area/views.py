from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.

def area(request):
    infos = areas.objects.all()
    context = {
        "beijing": infos,
    }
    for i in infos:
        print(type(i))
    return render(request, "area/area.html", context)
