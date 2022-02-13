from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("hello world!")


def add(request):
    return HttpResponse("add.......")


def find(request, sid=0, name=""):
    return HttpResponse(f"find.........{sid}{name}")


def update(request):
    return HttpResponse("update.......")


def fun(request, yy, mm):
    return HttpResponse("参数信息：%s年%s月" % (yy, mm))
