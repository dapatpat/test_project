# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from datetime import *
from .models import *
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    return render(request, 'sim_system/index_base.html')


def selection(request):
    newstudent = stuInfos()
    allstudents = stuInfos.objects.all()
    temp_stu_no = request.POST["stu_no"]
    if temp_stu_no != "":
        try:
            stu = stuInfos.objects.get(stu_no=temp_stu_no)
        except Exception:
            return HttpResponse("查无此人")
        else:
            context = {
                "stu": stuInfos.objects.get(stu_no=temp_stu_no),
            }
            return render(request, "sim_system/selection.html", context)
    else:
        for stu in allstudents:
            print(stu.stu_name)
        context = {
            "allstudents": allstudents,
        }
        return render(request, "sim_system/all.html", context)


def addInfos(request):
    newstudent = stuInfos()
    allstudents = stuInfos.objects.all()
    allsubjects = subInfos.objects.all()
    for sub in allsubjects:
        print(sub)
    try:
        stuInfos.objects.get(stu_no=request.POST["num"])
    except Exception:
        newstudent.stu_no = request.POST["num"]
        newstudent.stu_name = request.POST["name"]
        newstudent.stu_age = request.POST["age"]
        newstudent.stu_gender = request.POST["gender"]
        newstudent.stu_duty = request.POST["duty"]
        newstudent.save()

        # sub = subInfos.objects.get(sub_name=request.POST["subname"])
        # sub = subInfos.objects.get(sub_no=)
        # stu = stuInfos.objects.get(stu_no=stuno)
        # newsubject.stu_no = stu
        # newsubject.save()
        context = {
            "newstudentstu_no": newstudent.stu_no,
            "newstudentstu_name": newstudent.stu_name,
            "newstudentstu_age": newstudent.stu_age,
            "newstudentstu_gender": newstudent.stu_gender,
            "newstudentstu_duty": newstudent.stu_duty,
            # "newsubjectsub_no":newsubject.sub_no,
            # "newsubjectsub_name":newsubject.sub_name,
        }
        return render(request, 'sim_system/addInfos.html', context)

    else:
        return HttpResponse("对不起,您输入的信息已存在")


def showall(request):

    allinfos = stuInfos.objects.all()
    allinfos = list(allinfos)
    print (allinfos[1])
    info_cut = Paginator(allinfos,10)
    firstpage = info_cut.page(1)
    context = {
        "allinfos": firstpage.object_list,
    }
    return render(request,"sim_system/showall.html",context)
