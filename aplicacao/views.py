from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Pessoa

def index(request):
    return HttpResponse("Hello world in Python Django 1.")

def coisa(request):
    return HttpResponse("Hello world in Python Django - Index 2222.")    

def coisadetails(request,coisaid):
    payload = {'dados':[{'id':coisaid}]}
    return JsonResponse(payload)

def pessoas(request):
	# recupera todas pessoas na base de dados
    db_pessoas = Pessoa.objects.todos().values()
    
    # cria paylot com array de pessoas
    payload = { 'todaspessoas' : list(db_pessoas) }
    
    # retorno em Json
    return JsonResponse(payload)
