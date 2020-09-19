from django.urls import path
from .views import viewsindex
from .views import viewspessoas
from .views import viewstelefones
from .views import viewsveiculos

urlpatterns = [
    path('', viewsindex.index, name='index'),
    path('pessoas/', viewspessoas.pessoas, name='pessoas'),
    path('pessoa/<int:pessoaid>', viewspessoas.pessoa, name='pessoa'),
    path('pessoa/cadastrar/nova', viewspessoas.newpessoa, name='newpessoa'),
    path('pessoa/deletar/<int:pessoaid>', viewspessoas.deletarpessoa, name='deletarpessoa'),
    path('pessoa/atualizar/<int:pessoaid>', viewspessoas.atualizarpessoa, name='atualizarpessoa'),
    path('pessoa/forminserepessoa', viewspessoas.forminserepessoa, name='forminserepessoa'),

    path('telefones/', viewstelefones.telefones, name='telefones'),
    path('telefone/<int:phoneid>', viewstelefones.telefone, name='telefone'),
    path('telefone/cadastrar/novo', viewstelefones.newtelefone, name='newtelefone'),
    path('telefone/deletar/<int:phoneid>', viewstelefones.deletartelefone, name='deletartelefone'),
    path('telefone/atualizar/<int:phoneid>', viewstelefones.atualizartelefone, name='atualizartelefone'),
    path('telefone/forminseretelefone', viewstelefones.forminseretelefone, name='forminseretelefone'),
    
    path('veiculos/', viewsveiculos.veiculos, name='veiculos'),
    path('veiculo/<int:vehicleid>', viewsveiculos.veiculo, name='veiculo'),
    path('veiculo/cadastrar/novo', viewsveiculos.newveiculo, name='newveiculo'),
    path('veiculo/deletar/<int:vehicleid>', viewsveiculos.deletarveiculo, name='deletarveiculo'),
    path('veiculo/atualizar/<int:vehicleid>', viewsveiculos.atualizarveiculo, name='atualizarveiculo'),
    path('veiculo/forminsereveiculo', viewsveiculos.forminsereveiculo, name='forminsereveiculo'),
]