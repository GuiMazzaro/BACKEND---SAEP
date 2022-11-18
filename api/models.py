from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class automoveis(models.Model):
    modelo = models.CharField(max_length=50)
    preco = models.IntegerField()

    def __str__(self):
        return self.modelo

class cliente(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class concessionaria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class area(models.Model):
    area = models.CharField(max_length=50)

    def __str__(self):
        return self.area

class venda(models.Model):
    cliente = models.ForeignKey(cliente, related_name="clientes", on_delete=models.CASCADE)
    concessionaria = models.ForeignKey(concessionaria, related_name="concessionarias", on_delete=models.CASCADE)

    def __str__(self):
        return self.cliente

class alocacao(models.Model):
    area = models.ForeignKey(area, related_name="areas", on_delete=models.CASCADE)
    automaveis = models.ForeignKey(automoveis, related_name="automoveis", on_delete=models.CASCADE)
    concessionaria = models.ForeignKey(concessionaria, related_name="concessionaria", on_delete=models.CASCADE)
    quantidade = models.CharField(max_length=10)

    def __str__(self):
        return self.area