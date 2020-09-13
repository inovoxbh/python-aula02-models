from rest_framework import serializers
from .models import Pessoa, Departamento

class PessoaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Pessoa
		fields = ('id', 'nome', 'sobrenome', 'idade')

class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Departamento
		fields = ('sigla', 'descricao')