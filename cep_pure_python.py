import requests
import pyodbc

def requisicao_api():
    try:
        while True:
            entrada = input("Digite o CEP do local que você quer: ")
            print ("Analisando o cep informado...")
            api_url = "https://brasilapi.com.br/api/cep/v1/"+entrada

            resposta = requests.get(api_url)

            
            if resposta.status_code == 200:
                dados = resposta.json()
                conexao_bdd(dados) 
            else:
                print("Erro ao fazer requisição. Código:", resposta.status_code)
            
            continuar = input("------------------------------------------\nDeseja adicionar outro CEP? (s/n) ")

            if continuar.lower() != 's':
                break

    except requests.exceptions.RequestException as e:
        print("Erro de requisição:", e)

def conexao_bdd(dados):
    dados_conexao = (
        "Driver={SQL Server};"
        "Server=ALDEANDER-PC;"
        "Database=PythonSQL;"
    )
    conexao = pyodbc.connect(dados_conexao)
    cursor = conexao.cursor()

    servico = dados['service']
    cep = dados['cep']
    cidade = dados['city']
    estado = dados['state']

    if 'street' in dados:
        logradouro = dados['street']
    else:
        logradouro = "Rua desconhecida"

    if 'neighborhood' in dados:
        bairro = dados['neighborhood']
    else:
        bairro = "Bairro desconhecido"


    comando = f"""INSERT INTO Enderecos(Servico, CEP, Logradouro, Bairro, Cidade, Estado)
            VALUES
	        ('{servico}', '{cep}', '{logradouro}', '{bairro}', '{cidade}', '{estado}')"""
    
    cursor.execute(comando)
    cursor.commit()


def imprimir_dados():
    dados_conexao = (
        "Driver={SQL Server};"
        "Server=ALDEANDER-PC;"
        "Database=PythonSQL;"
    )

    conexao = pyodbc.connect(dados_conexao)
    cursor = conexao.cursor()
    cursor.execute("SELECT Servico, CEP, Logradouro, Bairro, Cidade, Estado FROM Enderecos")

    print("Seus endereços solicitados foram:")
    for linha in cursor.fetchall():
        print("Serviço:", linha[0])
        print("CEP:", linha[1])
        print("Logradouro:", linha[2])
        print("Bairro:", linha[3])
        print("Cidade:", linha[4], ",", linha[5])
        print ("------------------------------------------")

def limpar_banco():
    dados_conexao = (
        "Driver={SQL Server};"
        "Server=ALDEANDER-PC;"
        "Database=PythonSQL;"
    )
    conexao = pyodbc.connect(dados_conexao)
    cursor = conexao.cursor()

    comando = "DELETE FROM Enderecos"
    cursor.execute(comando)
    conexao.commit()

requisicao_api()
imprimir_dados()

limpar_banco()