from statistics import mode
from django.db import models


class TipoAcomodacao(models.Model):
    tipo = models.CharField(max_length=60)
    imagem = models.ImageField(null=True)
    descricao = models.CharField(max_length=100, null=True)
    valor= models.FloatField(null=True)
    def __str__(self) -> str:
        return self.tipo

class Cliente(models.Model):
    nome = models.CharField(max_length=60)
    def __str__(self) -> str:
        return self.nome

class Acomodacao(models.Model):
    descricao = models.CharField(max_length=100)
    categoria = models.ForeignKey(TipoAcomodacao, on_delete=models.PROTECT)
    cliente = models.ManyToManyField(Cliente)


# Create your models here.
