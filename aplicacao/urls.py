from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pessoas/', views.pessoas, name='pessoas'),
    path('pessoa/<int:pessoaid>', views.pessoa, name='pessoa'),
    path('pessoa/newpessoa', views.newpessoa, name='newpessoa'),
    path('coisa/', views.coisa, name='coisa'),
    path('coisa/<int:coisaid>', views.coisadetails, name='coisadetails'),
]