import pytest
import sys
import os

# --- SOLUÇÃO DE CAMINHO ---
# 1. Obtém o diretório atual (onde está o conftest.py)
current_dir = os.path.dirname(os.path.abspath(__file__))
# 2. Navega para o diretório raiz (subindo um nível de 'tests')
root_dir = os.path.join(current_dir, '..')
# 3. Adiciona o diretório raiz ao caminho de módulos do Python
# Isso permite que 'from src.app import app' funcione corretamente.
sys.path.insert(0, root_dir)
# -------------------------

# Importação do seu aplicativo Flask
# Se o seu arquivo principal se chama 'app.py' dentro da pasta 'src', 
# esta importação é a correta:
from src.app import app 

@pytest.fixture
def client():
    """Configura um cliente de teste para a aplicação Flask."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
        
