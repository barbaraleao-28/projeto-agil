# Importa o fixture 'client' que configuramos no conftest.py
# O Pytest encontra automaticamente o fixture
# from .conftest import client # (Se conftest.py estiver no mesmo nível)

def test_home_page_status(client):
    """Testa se a página inicial está acessível (status 200)."""
    # client.get('/') simula uma requisição GET para a rota '/'
    response = client.get('/') 
    
    # Garante que a requisição foi bem sucedida
    assert response.status_code == 200
    
    # Garante que a resposta contém um texto esperado (ex: o título da página)
    assert b"Lista de Tarefas" in response.data 

def test_create_task_success(client):
    """Testa a criação de uma nova tarefa via POST."""
    
    # Dados que seriam enviados pelo formulário (ajuste os nomes dos campos!)
    task_data = {
        'title': 'Tarefa de Teste',
        'description': 'Precisa ser concluída',
        # Incluir o novo campo de escopo (ex: 'due_date': '2025-12-31')
    }
    
    # Simula a submissão do formulário (POST)
    response = client.post('/add', data=task_data, follow_redirects=True)
    
    # Garante que a criação foi bem sucedida (Redirecionamento para a Home/Lista)
    assert response.status_code == 200 
    
    # Garante que a nova tarefa aparece na página (o 'Read' após o 'Create')
    assert b"Tarefa de Teste" in response.data 

def test_mark_task_as_done(client):
    """
    Testa a alteração de status da tarefa (Marcar como Concluída).
    Este teste é crucial para a funcionalidade principal.
    """
    # Este teste assume que já existe uma tarefa (pode ser criada em um fixture temporário)
    
    # 1. Cria uma tarefa para garantir que ela exista (opcional, ou use um fixture)
    client.post('/add', data={'title': 'Tarefa para Marcar', 'description': 'Teste Status'})

    # 2. Simula a requisição para marcar a tarefa como concluída (ex: rota /complete/1)
    # Você precisará do ID da tarefa, o que pode exigir uma busca ou mock.
    # Assumindo uma rota simples de "toggle" para a tarefa de ID 1:
    response = client.post('/complete/1', follow_redirects=True) 

    assert response.status_code == 200
    # Verifica se o status mudou (você teria que checar a classe CSS ou texto 'Concluída')
    # assert b"Concluída" in response.data 
    
def test_delete_task(client):
    """Testa a exclusão de uma tarefa."""
    
    # 1. Simula a exclusão (POST para a rota /delete/1)
    response = client.post('/delete/1', follow_redirects=True)
    
    assert response.status_code == 200
    # 2. Garante que o item não está mais na lista
    assert b"Tarefa de Teste" not in response.data 

### ✅ Ações a Fazer:

1.  **Criar Arquivos:** Crie (ou atualize) o arquivo `conftest.py` e o `test_tasks.py` (ou similar) na sua pasta `/tests`.
2.  **Commit Semântico:** Após a implementação, registre no GitHub:
    > `test: Implementa testes funcionais para o CRUD de tarefas`
3.  **Documentação:** Use a explicação sobre esses testes (que simulam o usuário interagindo com as rotas) para preencher a seção **"Explicação sobre os testes automatizados utilizados"** na sua **Parte Teórica (1)**.

Qual desses pontos (Testes, Vídeo Pitch, ou o preenchimento final do documento) você gostaria de focar agora?
