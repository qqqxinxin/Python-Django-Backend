from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<em>My second Project</em>")


def help(request):
    helpdict={'help_insert':'HELP PAGE in views.py file'}
    return render(request,'appTwo/help.html',context=helpdict)
