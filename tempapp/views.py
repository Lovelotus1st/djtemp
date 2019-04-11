from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello there !!")

def temp_demo(request):
    dist_var ={'any_key': "Hello !! this is a value for the key from view.py that can be used in index.html"}
    return render(request,'index.html', context=dist_var)