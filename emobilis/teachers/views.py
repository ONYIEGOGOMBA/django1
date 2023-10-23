# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to emobilis")

def about(request):
    return HttpResponse("About emobilis")
