import requests
from django.shortcuts import HttpResponse
from app_enderecos.models import Endereco

def obter_enderecos(request, cep):
    url = f"https://brasilapi.com.br/api/cep/v1/{cep}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        endereco = Endereco.objects.create(
            cep=data.get('cep', ''),
            state=data.get('state', ''),
            city=data.get('city', ''),
            neighborhood=data.get('neighborhood', ''),
            street=data.get('street', ''),
            service=data.get('service', '')
        )

        return HttpResponse("Endereço externo salvo com sucesso!")
    else:
        return HttpResponse("Erro ao obter endereço externo.")
