from django.db import models

# Create your models here.



class AreasTecnologicas(models.Model):

    nome = models.CharField(max_length = 100)

    def __str__(self):
        return self.nome


class Financiadores(models.Model):

    nome = models.CharField(max_length = 100)

    def __str__(self):
        return self.nome


class Colaboradores(models.Model):

    cpf = models.CharField(max_length = 14)
    nome = models.CharField(max_length = 100)
    data_nascimento = models.DateField()

    def __str__(self):
        return f"({self.cpf} {self.nome})"

       


class Projetos(models.Model):

    coordenador = models.CharField(max_length = 100)
    financiador = models.ManyToManyField(Financiadores)
    area_tecnologica = models.ManyToManyField(AreasTecnologicas)
    ativo = models.BooleanField()
    inicio_vigencia = models.DateField()
    fim_vigencia = models.DateField()
    valor = models.DecimalField(max_digits = 10, decimal_places = 2)
    quantidade_membros = models.IntegerField()
    equipe = models.ManyToManyField(Colaboradores)

    def __str__(self):
        return f"({self.coordenador} {self.financiador} {self.area_tecnologica} {self.ativo})"


