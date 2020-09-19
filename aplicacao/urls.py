from django.urls import path
from .views import viewsindex
from .views import viewspessoas
from .views import viewstelefones

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
    
]