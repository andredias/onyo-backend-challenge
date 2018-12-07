from django.db import models


class CEP(models.Model):
    cep = models.CharField(max_length=8, primary_key=True)
    logradouro = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    localidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return self.cep
