import pytest
import sys
import os

# Ajusta o caminho para importar corretamente o app principal
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.join(current_dir, '..')
sys.path.insert(0, root_dir)

from app import app

@pytest.fixture
def client():
    """Cria um cliente de teste para simular requisições HTTP na aplicação Flask."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

