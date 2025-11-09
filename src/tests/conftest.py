import pytest
# IMPORTAÇÃO CORRETA, POIS O CI AGORA SABE ONDE ENCONTRAR 'src'
from src.app import app 

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
