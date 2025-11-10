import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.app import app  # Corrigido!

@pytest.fixture
def cliente():
    app.testing = True
    return app.test_client()

def test_home(cliente):
    resposta = cliente.get('/')
    assert resposta.status_code == 200
    assert b"Bem-vinda ao TechFlow" in resposta.data  # corrigido: sem exclamação extra

def test_listar_tarefas(cliente):
    resposta = cliente.get('/tarefas')
    assert resposta.status_code == 200
    assert b"Estudar Python" in resposta.data
