import pytest
import sys
import os

# Corrige o caminho para importar o app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


@pytest.fixture
def cliente():
    """Cria um cliente de teste para o Flask."""
    app.testing = True
    return app.test_client()


def test_home(cliente):
    """Testa a rota principal '/'."""
    resposta = cliente.get('/')
    assert resposta.status_code == 200
    # Usa get_data(as_text=True) para comparar texto com acento
    assert "Bem-vinda ao TechFlow" in resposta.get_data(as_text=True)


def test_listar_tarefas(cliente):
    """Testa a listagem de tarefas."""
    resposta = cliente.get('/tarefas')
    assert resposta.status_code == 200
    assert "Estudar Python" in resposta.get_data(as_text=True)
