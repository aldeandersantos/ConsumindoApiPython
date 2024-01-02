import requests
import pyodbc

def requisicao_api():
    try:
        entrada = input("Digite o CEP do local que você quer: ")
        api_url = "https://brasilapi.com.br/api/cep/v1/"+entrada

        resposta = requests.get(api_url)

        
        if resposta.status_code == 200:
            dados = resposta.json()
            conexao_bdd(dados) 
        else:
            print("Erro ao fazer requisição. Código:", resposta.status_code)
        

    except requests.exceptions.RequestException as e:
        print("Erro de requisição:", e)

def conexao_bdd(dados):
    dados_conexao = (
        "Driver={SQL Server};"
        "Server=ALDEANDER-PC;"
        "Database=PythonSQL;"
    )
    conexao = pyodbc.connect(dados_conexao)
    print("Conexão bem sucedida!")
    cursor = conexao.cursor()

    servico = dados['service']
    cep = dados['cep']
    logradouro = dados['street']
    bairro = dados['neighborhood']
    cidade = dados['city']
    estado = dados['state']


    comando = f"""INSERT INTO Enderecos(Servico, CEP, Logradouro, Bairro, Cidade, Estado)
            VALUES
	        ('{servico}', '{cep}', '{logradouro}', '{bairro}', '{cidade}', '{estado}')"""
    
    cursor.execute(comando)
    cursor.commit()


requisicao_api()