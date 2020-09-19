from django.http import HttpResponse
from django.http import JsonResponse
from aplicacao.models import Departamento
from django.views.decorators.csrf import csrf_exempt
from django.http.multipartparser import MultiPartParser
from django.template import loader
from django.shortcuts import render

# REST e Template: retorna todas os departamentos
def departamentos(request):
	# recupera todos departamentos na base de dados
    db_departamentos = Departamento.objects.todos().values()
    
    # cria payload com array de departamentos
    payload = { 'todosdepartamentos' : list(db_departamentos) }

    # retorno em Json
    #return JsonResponse(payload)

    # retorno via template
    template = loader.get_template('departamento/listardepartamentos.html')
    return HttpResponse(template.render(payload, request))

def departamento(request,deptoid):
    if (request.method == 'GET'):
        # recupera um departamento específico na base de dados
        db_departamento = Departamento.objects.adepto(deptoid=deptoid).values()
        
        # cria payload com o departamento
        payload = { 'departamento' : list(db_departamento) }
        print(payload)
        
        # retorno em Json
        #return JsonResponse(payload)

        # retorno via template
        template = loader.get_template('departamento/detalhardepartamento.html')
        return HttpResponse(template.render(payload, request))

# REST: inclui departamento
@csrf_exempt
def newdepartamento(request):
    # dados enviados via Postman - Body - form-data
    alldata = request.POST
    
    # extrai dados enviados na requisição
    reqSigla = alldata.get("sigla", "0")
    reqDescricao = alldata.get("descricao", "0")
    # thanks to: https://stackoverflow.com/questions/10023213/extracting-items-out-of-a-querydict/14093989#14093989
    
    # instancia novo departamento
    p = Departamento(sigla=reqSigla,descricao=reqDescricao)
    
    # grava novo departamento no banco
    p.save()
    
    #return HttpResponse("Inserido com sucesso!")

    payload = { 'mensagem' : "Cadastro inserido com sucesso!" }
    template = loader.get_template('msgfeedback.html')
    return HttpResponse(template.render(payload, request))

# template: exclui departamento
def deletardepartamento(request,deptoid):
    db_departamento = Departamento.objects.adepto(deptoid=deptoid)
    db_departamento.delete()

    payload = { 'mensagem' : "Cadastro excluído com sucesso!" }
    template = loader.get_template('msgfeedback.html')
    return HttpResponse(template.render(payload, request))

# template: atualizar departamento
@csrf_exempt
def atualizardepartamento(request,deptoid):
    if (request.method == 'GET'):
        db_departamento = Departamento.objects.adepto(deptoid=deptoid)
        payload = { 'departamento' : list(db_departamento) }

        template = loader.get_template('departamento/atualizardepartamento.html')
        return HttpResponse(template.render(payload, request))

    if (request.method == 'POST'):
        # recupera departamento no banco de dados
        db_departamento = Departamento.objects.get(id=deptoid)

        # extrai dados enviados na requisição
        alldata = request.POST

        # atualiza dados conforme parâmetro da requisição
        db_departamento.sigla = alldata.get("sigla", "0")
        db_departamento.descricao = alldata.get("descricao", "0")

        # salva departamento alterada no banco
        db_departamento.save()

        payload = { 'mensagem' : "Cadastro atualizado com sucesso!" }
        template = loader.get_template('msgfeedback.html')
        return HttpResponse(template.render(payload, request))

# template:insere departamento
@csrf_exempt
def forminseredepartamento(request):
    return render(request, 'departamento/inserirdepartamento.html')
