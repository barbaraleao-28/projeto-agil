# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de tarefas
tarefas = [
    {"id": 1, "titulo": "Estudar Python", "feito": False},
    {"id": 2, "titulo": "Criar projeto ágil", "feito": False}
]

@app.route('/')
def home():
    return jsonify({"mensagem": "Bem-vinda ao TechFlow!"})

@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas)

@app.route('/tarefas', methods=['POST'])
def adicionar_tarefa():
    nova = request.get_json()
    tarefas.append(nova)
    return jsonify(nova), 201

if __name__ == '__main__':
    app.run(debug=True)
