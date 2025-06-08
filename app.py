from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = []
next_id = 1

@app.route('/')
def home():
    return "Minha API de DevOps está ativa e funcionando!!!", 200

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios), 200

@app.route('/usuarios', methods=['POST'])
def adicionar_usuario():
    global next_id
    dados = request.get_json()
    if not dados or "nome" not in dados or "idade" not in dados:
        return jsonify({"erro": "Dados inválidos"}), 400
    usuario = {"id": next_id, "nome": dados["nome"], "idade": dados["idade"]}
    usuarios.append(usuario)
    next_id += 1
    return jsonify(usuario), 201

@app.route('/usuarios/<int:id_usuario>', methods=['GET'])
def buscar_usuario(id_usuario):
    for usuario in usuarios:
        if usuario["id"] == id_usuario:
            return jsonify(usuario), 200
    return jsonify({"erro": "Usuário não encontrado"}), 404