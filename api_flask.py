from flask import Flask, jsonify, request

app = Flask(__name__)

enderecos = [
    {
        'id': 1,
        'cep': '12243000',
        'state': 'SP',
        'city': 'São José dos Campos',
        'neighborhood': 'Jardim Apolo I',
        'street': 'Avenida Nove de Julho - lado ímpar',
        'service': 'widenet'
    },
    {
        'id': 2,
        'cep': '59015450',
        'state': 'RN',
        'city': 'Natal',
        'neighborhood': 'Tirol',
        'street': 'Avenida Nevaldo Rocha - de 3593 a 4785 - lado ímpar',
        'service': 'widenet'
    },
    {
        'id': 3,
        'cep': '59380000',
        'state': 'RN',
        'city': 'Currais Novos',
        'service': 'correios'
    },
]

    
@app.route('/enderecos',methods=['GET'])

def obter_endereco():
    return jsonify(enderecos)

@app.route('/enderecos/<int:id>', methods=['GET'])

def obter_enderecos_por_id(id):
    for endereco in enderecos:
        if endereco.get('id') == id:
            return jsonify(endereco)
    return jsonify({'mensagem': 'Endereço não encontrado'}), 404

@app.route('/enderecos', methods=['POST'])
def incluir_novo_endereco():
    global enderecos
    novo_endereco = request.get_json()
    enderecos.append(novo_endereco)
    ultimo_indice = len(enderecos) - 1
    return jsonify({'endereco': enderecos[ultimo_indice]})




@app.route('/enderecos/<int:id>', methods=['PUT'])

def editar_endereco_por_id(id):
    global enderecos
    endereco_alterado = request.get_json()
    for indice, endereco in enumerate(enderecos):
        if endereco.get('id') == id:
            enderecos[indice].update(endereco_alterado)
            return jsonify(enderecos[indice])
    return jsonify({'mensagem': 'Endereço não encontrado'}), 404


@app.route('/enderecos/<int:id>', methods=['DELETE'])
def excluir_endereco(id):
    for indice, endereco in enumerate(enderecos):
        if endereco.get('id') == id:
            del enderecos[indice]
            return jsonify({'mensagem': 'Endereço deletado com sucesso!'})

    return jsonify({'mensagem': 'Endereço não encontrado'}), 404

app.run(port=5000,host='localhost', debug=True)