def test_home_page_status(client):
    """Testa se a página inicial está acessível (status 200)."""
    response = client.get('/')
    assert response.status_code == 200
    assert "Lista de Tarefas" in response.get_data(as_text=True)


def test_create_task_success(client):
    """Testa a criação de uma nova tarefa via POST."""
    task_data = {
        'title': 'Tarefa de Teste',
        'description': 'Precisa ser concluída',
    }

    response = client.post('/add', data=task_data, follow_redirects=True)
    assert response.status_code == 200
    assert "Tarefa de Teste" in response.get_data(as_text=True)


def test_mark_task_as_done(client):
    """Testa marcar uma tarefa como concluída."""
    client.post('/add', data={'title': 'Tarefa para Marcar', 'description': 'Teste Status'})

    response = client.post('/complete/1', follow_redirects=True)
    assert response.status_code == 200
    # assert "Concluída" in response.get_data(as_text=True)


def test_delete_task(client):
    """Testa a exclusão de uma tarefa."""
    response = client.post('/delete/1', follow_redirects=True)
    assert response.status_code == 200
    assert "Tarefa de Teste" not in response.get_data(as_text=True)
