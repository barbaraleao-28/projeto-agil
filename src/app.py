from flask import Flask, jsonify, request, redirect, url_for

app = Flask(__name__)

tarefas = [
    {"id": 1, "titulo": "Estudar Python", "feito": False},
    {"id": 2, "titulo": "Criar projeto ágil", "feito": False}
]

@app.route('/')
def home():
    return jsonify({"mensagem": "Lista de Tarefas"})

@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas)

@app.route('/add', methods=['POST'])
def adicionar_tarefa():
    nova_tarefa = request.form.to_dict()
    nova_tarefa['id'] = len(tarefas) + 1
    nova_tarefa['feito'] = False
    tarefas.append(nova_tarefa)
    return redirect(url_for('listar_tarefas'))

@app.route('/complete/<int:id>', methods=['POST'])
def marcar_como_concluida(id):
    for tarefa in tarefas:
        if tarefa['id'] == id:
            tarefa['feito'] = True
            break
    return redirect(url_for('listar_tarefas'))

@app.route('/delete/<int:id>', methods=['POST'])
def excluir_tarefa(id):
    global tarefas
    tarefas = [t for t in tarefas if t['id'] != id]
    return redirect(url_for('listar_tarefas'))

if __name__ == '__main__':
    app.run(debug=True)

