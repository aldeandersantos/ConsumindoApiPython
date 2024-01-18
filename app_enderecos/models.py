from django.db import models

class Endereco(models.Model):
    cep = models.CharField(max_length=10)
    logradouro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.logradouro
