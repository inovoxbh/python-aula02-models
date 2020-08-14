from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coisa/', views.coisa, name='coisa'),
]