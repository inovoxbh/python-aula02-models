from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world in Python Django.")

def coisa(request):
    return HttpResponse("Hello world in Python Django - Index 2.")    