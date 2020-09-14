from django.contrib import admin
from .models import Departamento,Pessoa,Veiculo,Telefone

admin.site.register(Pessoa)
admin.site.register(Departamento)
admin.site.register(Veiculo)
admin.site.register(Telefone)