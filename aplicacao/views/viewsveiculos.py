from django.http import HttpResponse
from django.http import JsonResponse
from aplicacao.models import Veiculo
from django.views.decorators.csrf import csrf_exempt
from django.http.multipartparser import MultiPartParser
from django.template import loader
from django.shortcuts import render

# REST e Template: retorna todas os veiculos
def veiculos(request):
	# recupera todos veiculos na base de dados
    db_veiculos = Veiculo.objects.todos().values()
    
    # cria payload com array de veiculos
    payload = { 'todosveiculos' : list(db_veiculos) }

    # retorno em Json
    #return JsonResponse(payload)

    # retorno via template
    template = loader.get_template('veiculo/listarveiculos.html')
    return HttpResponse(template.render(payload, request))

def veiculo(request,vehicleid):
    if (request.method == 'GET'):
        # recupera um veiculo específico na base de dados
        db_veiculo = Veiculo.objects.avehicle(vehicleid=vehicleid).values()
        
        # cria payload com o veiculo
        payload = { 'veiculo' : list(db_veiculo) }
        print(payload)
        
        # retorno em Json
        #return JsonResponse(payload)

        # retorno via template
        template = loader.get_template('veiculo/detalharveiculo.html')
        return HttpResponse(template.render(payload, request))

# REST: inclui veiculo
@csrf_exempt
def newveiculo(request):
    # dados enviados via Postman - Body - form-data
    alldata = request.POST
    
    # extrai dados enviados na requisição
    reqModelo = alldata.get("modelo", "0")
    reqFabricacao = alldata.get("fabricacao", "0")
    reqProprietario = alldata.get("proprietario_id", "0")
    reqPlaca = alldata.get("placa","0")
    # thanks to: https://stackoverflow.com/questions/10023213/extracting-items-out-of-a-querydict/14093989#14093989
    
    # instancia novo veiculo
    p = Veiculo(modelo=reqModelo,fabricacao=reqFabricacao,proprietario_id=reqProprietario,placa=reqPlaca)
    
    # grava novo veiculo no banco
    p.save()
    
    #return HttpResponse("Inserido com sucesso!")

    payload = { 'mensagem' : "Cadastro inserido com sucesso!" }
    template = loader.get_template('msgfeedback.html')
    return HttpResponse(template.render(payload, request))

# template: exclui veiculo
def deletarveiculo(request,vehicleid):
    db_veiculo = Veiculo.objects.avehicle(vehicleid=vehicleid)
    db_veiculo.delete()

    payload = { 'mensagem' : "Cadastro excluído com sucesso!" }
    template = loader.get_template('msgfeedback.html')
    return HttpResponse(template.render(payload, request))

# template: atualizar veiculo
@csrf_exempt
def atualizarveiculo(request,vehicleid):
    if (request.method == 'GET'):
        db_veiculo = Veiculo.objects.avehicle(vehicleid=vehicleid)
        payload = { 'veiculo' : list(db_veiculo) }

        template = loader.get_template('veiculo/atualizarveiculo.html')
        return HttpResponse(template.render(payload, request))

    if (request.method == 'POST'):
        # recupera veiculo no banco de dados
        db_veiculo = Veiculo.objects.get(id=vehicleid)

        # extrai dados enviados na requisição
        alldata = request.POST

        # atualiza dados conforme parâmetro da requisição
        db_veiculo.modelo = alldata.get("modelo", "0")
        db_veiculo.fabricacao = alldata.get("fabricacao", "0")
        db_veiculo.proprietario_id = alldata.get("proprietario_id", "0")
        db_veiculo.placa = alldata.get("placa","0")

        # salva veiculo alterada no banco
        db_veiculo.save()

        payload = { 'mensagem' : "Cadastro atualizado com sucesso!" }
        template = loader.get_template('msgfeedback.html')
        return HttpResponse(template.render(payload, request))

# template:insere veiculo
@csrf_exempt
def forminsereveiculo(request):
    return render(request, 'veiculo/inserirveiculo.html')
