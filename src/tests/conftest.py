import pytest
import sys
import os

# Adiciona a pasta 'src' ao caminho de importação do Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Importa o app do seu arquivo app.py
from src.app import app 

@pytest.fixture
def client():
    # ... (Resto do código do fixture)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
