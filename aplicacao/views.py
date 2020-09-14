from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Pessoa
from django.views.decorators.csrf import csrf_exempt
import json

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
    
    # cria payload com array de pessoas
    payload = { 'todaspessoas' : list(db_pessoas) }

    # retorno em Json
    return JsonResponse(payload)

@csrf_exempt
def pessoa(request,pessoaid):
    if (request.method == 'GET'):
        # recupera uma pessoa específica na base de dados
        db_pessoa = Pessoa.objects.aperson(pessoaid=pessoaid).values()
        
        # cria payload com a pessoa
        payload = { 'pessoa' : list(db_pessoa) }
        
        # retorno em Json
        return JsonResponse(payload)
    else:
        if (request.method == 'DELETE'):
            db_pessoa = Pessoa.objects.aperson(pessoaid=pessoaid)
            db_pessoa.delete()
            return HttpResponse("Excluido com sucesso!")

@csrf_exempt
def newpessoa(request):
    alldata = request.POST
    reqNome = alldata.get("nome", "0")
    reqSobrenome = alldata.get("sobrenome", "0")
    reqIdade = alldata.get("idade", "0")
    reqCPF = alldata.get("cpf","0")
    reqSexo = alldata.get("sexo","0")
    p = Pessoa(nome=reqNome,sobrenome=reqSobrenome,idade=reqIdade,cpf=reqCPF,sexo=reqSexo)
    p.save()
    return HttpResponse("Inserido com sucesso!")