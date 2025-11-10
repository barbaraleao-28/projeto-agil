import pytest
import sys
import os

# --- Ajuste de Caminho ---
# 1. Obtém o diretório atual (onde está o conftest.py)
current_dir = os.path.dirname(os.path.abspath(__file__))
# 2. Sobe um nível para alcançar o diretório raiz do projeto
root_dir = os.path.join(current_dir, '..')
# 3. Adiciona o diretório raiz ao caminho de módulos do Python
#    Isso permite importar 'src.app' corretamente
sys.path.insert(0, root_dir)
# --------------------------

# Importa a aplicação Flask do arquivo src/app.py
from src.app import app

@pytest.fixture
def client():
    """Configura um cliente de teste para a aplicação Flask."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
