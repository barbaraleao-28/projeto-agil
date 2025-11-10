import pytest

def test_home_page_status(client):
    """Testa se a rota inicial retorna mensagem JSON e status 200."""
    response = client.get('/')
    assert response.status_code == 200
    assert b" Seja bem-vindo ao TechFlow" in response.data

def test_listar_tarefas(client):
    """Testa se a rota /tarefas retorna a lista de tarefas corretamente."""
    response = client.get('/tarefas')
    assert response.status_code == 200
    assert b"Estudar Python" in response.data
    assert b"Criar projeto ágil" in response.data

def test_adicionar_tarefa(client):
    """Testa a criação de uma nova tarefa via POST."""
    nova_tarefa = {"id": 3, "titulo": "Testar API", "feito": False}
    response = client.post('/tarefas', json=nova_tarefa)
    assert response.status_code == 201
    assert b"Testar API" in response.data
