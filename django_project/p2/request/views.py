from django.shortcuts import render


# Create your views here.

def get(request):
    return render(request, "request/get.html")


def get1(request):
    aa = request.GET["a"]
    bb = request.GET["b"]
    context = {"aa": aa, 'bb': bb}
    return render(request, "request/get1.html", context)

def get2(request):
    alist = request.GET.getlist("a")
    blist = request.GET.getlist("b")
    context = {"a":alist,'b':blist}
    return render(request,"request/get2.html",context)
