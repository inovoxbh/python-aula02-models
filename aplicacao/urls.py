from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pessoas/', views.pessoas, name='pessoas'),
    path('coisa/', views.coisa, name='coisa'),
    path('coisa/<int:coisaid>', views.coisadetails, name='coisadetails'),
]