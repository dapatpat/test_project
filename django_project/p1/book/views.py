#coding=utf-8
from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    books = BookInfos.objects.all()
    heros = HeroInfos.objects.all()
    context = {'books':books,'heros':heros}
    return render(request,'book/index.html',context)
