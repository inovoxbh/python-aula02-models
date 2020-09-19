from django.http import HttpResponse
from django.http import JsonResponse
from .models import Pessoa
from django.views.decorators.csrf import csrf_exempt
from django.http.multipartparser import MultiPartParser
from django.template import loader
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello world in Python Django")

# REST e Template: retorna todas as pessoas
def pessoas(request):
	# recupera todas pessoas na base de dados
    db_pessoas = Pessoa.objects.todos().values()
    
    # cria payload com array de pessoas
    payload = { 'todaspessoas' : list(db_pessoas) }

    # retorno em Json
    #return JsonResponse(payload)

    # retorno via template
    template = loader.get_template('pessoa/listarpessoas.html')
    return HttpResponse(template.render(payload, request))

# REST: detalha, deleta e atualiza pessoa
@csrf_exempt
def pessoa(request,pessoaid):
    if (request.method == 'GET'):
        # recupera uma pessoa específica na base de dados
        db_pessoa = Pessoa.objects.aperson(pessoaid=pessoaid).values()
        
        # cria payload com a pessoa
        payload = { 'pessoa' : list(db_pessoa) }
        
        # retorno em Json
        #return JsonResponse(payload)

        # retorno via template
        template = loader.get_template('pessoa/detalharpessoa.html')
        print(payload)
        return HttpResponse(template.render(payload, request))


    if (request.method == 'DELETE'):
        db_pessoa = Pessoa.objects.aperson(pessoaid=pessoaid)
        db_pessoa.delete()
        return HttpResponse("Excluido com sucesso!")

    if (request.method == 'PUT'):
        # dados enviados via Postman - Body - form-data
        put_data = MultiPartParser(request.META, request, request.upload_handlers).parse()
        alldata = put_data[0]
        # thanks to: https://stackoverflow.com/questions/44927998/how-to-access-data-form-in-put-request-of-class-based-views-in-django
        
        # recupera pessoa no banco de dados
        db_pessoa = Pessoa.objects.get(id=pessoaid)

        # atualiza dados conforme parâmetro da requisição
        db_pessoa.nome = alldata.get("nome", "0")
        db_pessoa.sobrenome = alldata.get("sobrenome", "0")
        db_pessoa.idade = alldata.get("idade", "0")
        db_pessoa.cpf = alldata.get("cpf","0")
        db_pessoa.sexo = alldata.get("sexo","0")
        db_pessoa.deptoatual_id = alldata.get("depto_atual","0")

        # salva pessoa alterada no banco
        db_pessoa.save()
        
        return HttpResponse("Atualizado com sucesso!")

# REST: inclui pessoa
@csrf_exempt
def newpessoa(request):
    # dados enviados via Postman - Body - form-data
    alldata = request.POST
    
    # extrai dados enviados na requisição
    reqNome = alldata.get("nome", "0")
    reqSobrenome = alldata.get("sobrenome", "0")
    reqIdade = alldata.get("idade", "0")
    reqCPF = alldata.get("cpf","0")
    reqSexo = alldata.get("sexo","0")
    reqDeptoAtual = alldata.get("depto_atual","0")
    # thanks to: https://stackoverflow.com/questions/10023213/extracting-items-out-of-a-querydict/14093989#14093989
    
    # instancia nova pessoa
    p = Pessoa(nome=reqNome,sobrenome=reqSobrenome,idade=reqIdade,cpf=reqCPF,sexo=reqSexo,depto_atual_id=reqDeptoAtual)
    
    # grava nova pessoa no banco
    p.save()
    
    #return HttpResponse("Inserido com sucesso!")

    payload = { 'mensagem' : "Cadastro inserido com sucesso!" }
    template = loader.get_template('msgfeedback.html')
    return HttpResponse(template.render(payload, request))


# template: exclui pessoa
def deletarpessoa(request,pessoaid):
    db_pessoa = Pessoa.objects.aperson(pessoaid=pessoaid)
    db_pessoa.delete()

    payload = { 'mensagem' : "Cadastro excluído com sucesso!" }
    template = loader.get_template('msgfeedback.html')
    return HttpResponse(template.render(payload, request))

# template: atualizar pessoa
@csrf_exempt
def atualizarpessoa(request,pessoaid):
    if (request.method == 'GET'):
        db_pessoa = Pessoa.objects.aperson(pessoaid=pessoaid)
        payload = { 'pessoa' : list(db_pessoa) }

        template = loader.get_template('pessoa/atualizarpessoa.html')
        return HttpResponse(template.render(payload, request))

    if (request.method == 'POST'):
        # recupera pessoa no banco de dados
        db_pessoa = Pessoa.objects.get(id=pessoaid)

        # extrai dados enviados na requisição
        alldata = request.POST

        # atualiza dados conforme parâmetro da requisição
        db_pessoa.nome = alldata.get("nome", "0")
        db_pessoa.sobrenome = alldata.get("sobrenome", "0")
        db_pessoa.idade = alldata.get("idade", "0")
        db_pessoa.cpf = alldata.get("cpf","0")
        db_pessoa.sexo = alldata.get("sexo","0")
        db_pessoa.depto_atual_id = alldata.get("depto_atual","0")

        # salva pessoa alterada no banco
        db_pessoa.save()

        payload = { 'mensagem' : "Cadastro atualizado com sucesso!" }
        template = loader.get_template('msgfeedback.html')
        return HttpResponse(template.render(payload, request))

# template:insere pessoa
@csrf_exempt
def forminserepessoa(request):
    return render(request, 'pessoa/inserirpessoa.html')
