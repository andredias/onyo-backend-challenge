from django.db import models


class Funcionario(models.Model):
    cpf = models.CharField(max_length=11, primary_key=True)
    nome = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, null=True)
    bairro = models.CharField(max_length=200)
    localidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    class Meta:
        ordering = ('nome', )

    def __str__(self):
        return self.nome
