# test_app.py
import pytest
from src.app import app

@pytest.fixture
def cliente():
    app.testing = True
    return app.test_client()

def test_home(cliente):
    resposta = cliente.get('/')
    assert resposta.status_code == 200
    assert b"Bem-vinda ao TechFlow" in resposta.data

def test_listar_tarefas(cliente):
    resposta = cliente.get('/tarefas')
    assert resposta.status_code == 200
    assert b"Estudar Python" in resposta.data
