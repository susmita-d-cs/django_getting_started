from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def welcome(request):
    return HttpResponse("welcome Susmita")

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

#adding about page more details

def about(request):
    return HttpResponse("pluralsight coursework: Django beginners")