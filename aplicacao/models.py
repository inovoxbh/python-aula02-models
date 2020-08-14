from django.db import models

class Departamento(models.Model):
    sigla = models.CharField(max_length=6)
    descricao = models.CharField(max_length=30)

class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    idade = models.IntegerField(null=True)
    cpf = models.IntegerField(null=True)
    depto_atual = models.ForeignKey(
        Departamento,
        on_delete=models.RESTRICT,
        null=True
    )
    hist_deptos = models.ManyToManyField(
        Departamento,
        related_name='hist_pessoa_depto'
    )
    depto_chefia = models.OneToOneField(
        Departamento,
        on_delete=models.RESTRICT,
        null=True,
        related_name='chefia_dpto'
    )

    OPCOES_SEXO = [
        ('M','Masculino'),
        ('F','Feminino'),
        ('I','Indefinido')
    ]

    sexo = models.CharField(
        max_length=1,
        choices=OPCOES_SEXO,
        default='I'
    )