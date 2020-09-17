from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pessoas/', views.pessoas, name='pessoas'),
    path('pessoa/<int:pessoaid>', views.pessoa, name='pessoa'),
    path('pessoa/cadastrar/nova', views.newpessoa, name='newpessoa'),
    path('pessoa/deletar/<int:pessoaid>', views.deletarpessoa, name='deletarpessoa'),
    path('coisa/', views.coisa, name='coisa'),
    path('coisa/<int:coisaid>', views.coisadetails, name='coisadetails'),
]