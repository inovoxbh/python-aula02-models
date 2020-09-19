from django.db import models

class DepartamentoManager(models.Manager):
    def todos(self):
        result = self.all()
        return result

    def adepto(self,deptoid):
        result = self.filter(id=deptoid)
        return result

class Departamento(models.Model):
    sigla = models.CharField(max_length=6)
    descricao = models.CharField(max_length=30)

    def __str__ (self):
        return self.sigla + ' ' + self.descricao

    objects = DepartamentoManager()        

class PessoaManager(models.Manager):
    def create_pessoa(self, nome, sexo):
        pessoa = self.create(nome=nome, sexo=sexo)
        return pessoa

    def print_pessoa(self):
        print(self.none,self.sexo)

    # querie para retornar todas as pessoas
    def todos(self):
        result = self.all()
        return result

    # querie para retornar uma pessoa específica
    def aperson(self,pessoaid):
        result = self.filter(id=pessoaid)
        return result

    # querie para retornar pessoas do sexto masculino
    def homens(self):
        result = self.filter(sexo="M")
        return result

    # querie para retornar pessoas do sexto feminino
    def mulheres(self):
        result = self.filter(sexo="F")
        return result

    # querie para retornar pessoas com idade igual ou superior a 18 anos
    def adultos(self):
        result = self.filter(idade__gte=18)
        return result

    # querie para retornar pessoas com idade inferior a 18 anos
    def menores(self):
        result = self.filter(idade__lt=18)
        return result

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
        related_name='chefia_dpto',
        blank=True
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

    def __str__ (self):
        return f"{self.nome}  {self.sobrenome}, {self.idade} anos."

    objects = PessoaManager()

class VeiculoManager(models.Manager):
    def todos(self):
        result = self.all()
        return result

    def avehicle(self,vehicleid):
        result = self.filter(id=vehicleid)
        return result

class Veiculo(models.Model):
    placa = models.CharField(max_length=7)
    modelo = models.CharField(max_length=30)
    fabricacao = models.IntegerField(null=True)
    proprietario = models.ForeignKey(
        Pessoa,
        on_delete=models.RESTRICT,
        null=True
    )

    def __str__ (self):
        return f"{self.modelo} {self.fabricacao}, {self.placa}"

    objects = VeiculoManager()

class TelefoneManager(models.Manager):
    def todos(self):
        result = self.all()
        return result

    def aphone(self,phoneid):
        result = self.filter(id=phoneid)
        return result

class Telefone(models.Model):
    ddd = models.IntegerField(null=True)
    numero = models.IntegerField(null=True)
    proprietario = models.ForeignKey(
        Pessoa,
        on_delete=models.RESTRICT,
        null=True
    )

    OPCOES_TIPO_TELEFONE = [
        ('P','Pessoal'),
        ('C','Comercial'),
        ('I','Indefinido')
    ]

    tipo = models.CharField(
        max_length=1,
        choices=OPCOES_TIPO_TELEFONE,
        default='I'
    )

    def __str__ (self):
        return f"({self.ddd}) {self.numero}"

    objects = TelefoneManager()