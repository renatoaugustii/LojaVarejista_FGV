from django.db import models

# Create your models here.
class tab_cliente(models.Model):
    nomeCliente = models.CharField(max_length=60, blank=False)
    cpf = models.CharField(max_length=20,unique=True, blank=False, null=False)
    telefone = models.CharField(max_length=15, blank=False, unique=True)
    endereco = models.CharField(max_length=30, blank=True)
    pontos = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.nomeCliente


class tab_dependente(models.Model):
    nomeCliente = models.ForeignKey(tab_cliente, on_delete=models.CASCADE)
    nomeDependente = models.CharField(max_length=60, blank=False)
    parentesco = models.CharField(max_length=60, blank=False)
    def __str__(self):
        return self.nomeDependente