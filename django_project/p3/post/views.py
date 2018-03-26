# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from .models import *
from datetime import *

# Create your views here.

def index(request):
    return HttpResponse("Wellcome to Django!!")

def area(request):
    context={
        "test":"context  test "
    }
    return render(request,"area/area.html",context)




def handle(request):
    newtext = request.POST.get("a")
    if newtext != None:
        newdes = des()
        newdes.text = newtext
        newdes.save()
        print(newtext)
    return  redirect("/finish")

def liuyanban(request):
        alltext = des.objects.all()
        context = {
         "alltext":alltext,
        }
        return render(request,"liuyanban/liuyanban.php",context)





def post(request):
    return render(request,"post/post.html")

def post1(request):
    name = request.POST["name"]
    gender = request.POST["gender"]
    passwd = request.POST["passwd"]
    hobby = request.POST.getlist("hobby")
    context = {
        "name":name,"gender":gender,"passwd":passwd,"hobby":hobby
    }
    return render(request,'post/post1.html',context)

def cook(request):
    response = HttpResponse()
    if 'name' in request.COOKIES:
        response.write('<h1>'+"之前的cook是"+request.COOKIES['name']+'<h1/>')
    return response

def se(request):
    uname = request.session.get("newname")
    context = {"name":uname}
    return render(request,"post/se.html",context)

def session1(request):
    return render(request,"post/session1.html")

def session2(request):
    uname = request.POST["name"]
    request.session["newname"] = uname
    return redirect("/post/se")

def logout(request):
    del request.session["newname"]
    return redirect("/post/se")

