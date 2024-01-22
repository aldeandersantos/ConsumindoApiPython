from django.db import models

class Endereco(models.Model):
    cep = models.CharField(max_length=8, verbose_name="CEP", default="00000000")
    street = models.CharField(max_length=255, verbose_name="Logradouro", default="Rua Desconhecida", blank=True)
    city = models.CharField(max_length=100, verbose_name="Cidade", default="Capital")
    state = models.CharField(max_length=2, verbose_name="Estado", default="NA")
    neighborhood = models.CharField(max_length=50, verbose_name="Bairro", default="Bairro desconhecido", blank=True)
    service = models.CharField(max_length=50, verbose_name="Serviço", default="Servico desconhecido")
    endereco_ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.cep} | {self.street}"
