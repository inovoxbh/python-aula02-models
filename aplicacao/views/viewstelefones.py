from django.http import HttpResponse
from django.http import JsonResponse
from aplicacao.models import Telefone
from django.views.decorators.csrf import csrf_exempt
from django.http.multipartparser import MultiPartParser
from django.template import loader
from django.shortcuts import render

# REST e Template: retorna todas os telefones
def telefones(request):
	# recupera todos telefones na base de dados
    db_telefones = Telefone.objects.todos().values()
    
    # cria payload com array de telefones
    payload = { 'todostelefones' : list(db_telefones) }

    # retorno em Json
    #return JsonResponse(payload)

    # retorno via template
    template = loader.get_template('telefone/listartelefones.html')
    return HttpResponse(template.render(payload, request))

def telefone(request,phoneid):
    if (request.method == 'GET'):
        # recupera um telefone específico na base de dados
        db_telefone = Telefone.objects.aphone(phoneid=phoneid).values()
        
        # cria payload com o telefone
        payload = { 'telefone' : list(db_telefone) }
        print(payload)
        
        # retorno em Json
        #return JsonResponse(payload)

        # retorno via template
        template = loader.get_template('telefone/detalhartelefone.html')
        return HttpResponse(template.render(payload, request))

# REST: inclui telefone
@csrf_exempt
def newtelefone(request):
    # dados enviados via Postman - Body - form-data
    alldata = request.POST
    
    # extrai dados enviados na requisição
    reqDDD = alldata.get("ddd", "0")
    reqNumero = alldata.get("numero", "0")
    reqProprietario = alldata.get("proprietario", "0")
    reqTipo = alldata.get("tipo","0")
    # thanks to: https://stackoverflow.com/questions/10023213/extracting-items-out-of-a-querydict/14093989#14093989
    
    # instancia novo telefone
    p = Telefone(ddd=reqDDD,numero=reqNumero,proprietario_id=reqProprietario,tipo=reqTipo)
    
    # grava novo telefone no banco
    p.save()
    
    #return HttpResponse("Inserido com sucesso!")

    payload = { 'mensagem' : "Cadastro inserido com sucesso!" }
    template = loader.get_template('msgfeedback.html')
    return HttpResponse(template.render(payload, request))

# template: exclui telefone
def deletartelefone(request,phoneid):
    db_telefone = Telefone.objects.aphone(phoneid=phoneid)
    db_telefone.delete()

    payload = { 'mensagem' : "Cadastro excluído com sucesso!" }
    template = loader.get_template('msgfeedback.html')
    return HttpResponse(template.render(payload, request))

# template: atualizar telefone
@csrf_exempt
def atualizartelefone(request,phoneid):
    if (request.method == 'GET'):
        db_telefone = Telefone.objects.aphone(phoneid=phoneid)
        payload = { 'telefone' : list(db_telefone) }

        template = loader.get_template('telefone/atualizartelefone.html')
        return HttpResponse(template.render(payload, request))

    if (request.method == 'POST'):
        # recupera telefone no banco de dados
        db_telefone = Telefone.objects.get(id=phoneid)

        # extrai dados enviados na requisição
        alldata = request.POST

        # atualiza dados conforme parâmetro da requisição
        db_telefone.ddd = alldata.get("ddd", "0")
        db_telefone.numero = alldata.get("numero", "0")
        db_telefone.proprietario_id = alldata.get("proprietario_id", "0")
        db_telefone.tipo = alldata.get("tipo","0")

        # salva telefone alterada no banco
        db_telefone.save()

        payload = { 'mensagem' : "Cadastro atualizado com sucesso!" }
        template = loader.get_template('msgfeedback.html')
        return HttpResponse(template.render(payload, request))

# template:insere telefone
@csrf_exempt
def forminseretelefone(request):
    return render(request, 'telefone/inserirtelefone.html')
