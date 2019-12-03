
from django.http import HttpResponse
from django.shortcuts import render 

def homepage(request):
    return render(request,'word-count-home.html')


def home(request):
    return HttpResponse('hello')

def demohtml(request):
    return HttpResponse('<h1>hello<h1>')

def demoTemplate(request):
    return render(request,'home.html',{'key':'this value is passed in html page'})

def countwords(request):
    return render(request,'count.html')