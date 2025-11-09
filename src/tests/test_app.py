# test_app.py
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

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
