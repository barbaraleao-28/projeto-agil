import pytest
from seu_app import app # Ajuste 'seu_app' para o nome do seu arquivo principal do Flask (ex: app.py)

@pytest.fixture
def client():
    # Esta linha coloca o Flask em modo de teste
    app.config['TESTING'] = True
    
    # Cria um cliente de teste que pode fazer requisições (GET, POST, etc.)
    with app.test_client() as client:
        yield client # O cliente é retornado para ser usado nos testes
