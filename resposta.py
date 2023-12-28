import requests
import json

def requisicao_api():
    try:
        cep = input("Digite o CEP do local que você quer: ")
        api_url = "https://brasilapi.com.br/api/cep/v1/"+cep

        resposta = requests.get(api_url)

        if resposta.status_code == 200:
            dados = resposta.json()

            print("-----------------------")
            print("Serviço:", dados['service'])
            print("Cep:", dados['cep'][:5] + "-" + dados['cep'][5:])
            print("Logradouro:", dados['street'])
            print("Bairro:", dados['neighborhood'])
            print("Cidade:", dados['city']+", "+dados['state'])

        else:
            print("Erro ao fazer requisição. Código:", resposta.status_code)

    except requests.exceptions.RequestException as e:
        print("Erro de requisição:", e)
requisicao_api()