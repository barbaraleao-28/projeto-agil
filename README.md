# Atividade Projeto Ágil 

Para a execução da atividade proposta, foi feita a criação desse projeto que visa aplicar os conceitos de Engenharia de Software Ágil utilizando Python e GitHub.

## Objetivo Proposto
O objetivo da atividade é o desenvolvimento de um pequeno sistema de gerenciamento de tarefas, aplicando metodologias ágeis e também o controle de qualidade com testes automatizados e pipeline CI.

## Tecnologias utilizadas 
- Python 3.10
- Flask (para o sistema)
- Pytest (para os testes)
- GitHub Actions (para a automação)

## Estrutura inicial
/src → código-fonte principal
/tests → testes automatizados com Pytest
/docs → diagramas e documentação
.github/ → workflows de automação (CI)

## Metodologia usada
Foi usada nesse projeto uma abordagem Kanban conforme solicitada, com as seguintes etapas:
- A Fazer (to do)
- Em Progresso (Doing)
- Concluído (Done)

## Passos seguintes
1. Criar o quadro Kanban no GitHub Projects  
2. Adicionar as tarefas do projeto  
3. Criar a estrutura do código  
4. Implementar testes e pipeline  
5. Registrar prints e documentar o processo

---

## Mudança de Escopo

No processo de desenvolvimento, foi realizada uma **mudança de escopo** para incluir uma nova funcionalidade além do CRUD básico de tarefas.

###  Antes da mudança
O sistema permitia:
- Criar novas tarefas  
- Listar todas as tarefas existentes  
- Atualizar informações de uma tarefa  
- Excluir uma tarefa  

###  Após a mudança
Adicionou-se a funcionalidade de **filtrar tarefas por status**, permitindo visualizar separadamente:
- To Do (A fazer)
- In Progress  (Fazendo)
- Done  (Feito)

Essa mudança foi registrada como um novo card no **GitHub Projects**, acompanhada de um commit específico:

> "feat: adicionar filtro de tarefas por status"

Além disso, a nova funcionalidade foi testada com **Pytest** e validada automaticamente pelo **GitHub Actions**, garantindo o funcionamento correto da aplicação após a mudança.

---

## Conclusão

Este projeto demonstra a aplicação prática dos conceitos de **Engenharia de Software Ágil**, incluindo:
- Planejamento e versionamento de código  
- Uso do **Kanban** como ferramenta de organização  
- Implementação de **testes automatizados**  
- Execução de **integração contínua (CI)** com GitHub Actions  

A experiência reforça a importância da modelagem, colaboração e automação no ciclo de vida de um software, mesmo em projetos pequenos.

---


