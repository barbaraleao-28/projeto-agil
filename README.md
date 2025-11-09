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
No desenvolvimento do sistema de gerenciamento de tarefas, se identificou a necessidade de tornar a visualização mais prática e dinâmica.  
Então, foi implementado um **filtro por status das tarefas**, permitindo listar apenas as tarefas **"Em Progresso"** ou **"Concluídas"**.  

Essa alteração foi registrada como **mudança de escopo**, pois amplia a funcionalidade original do projeto, indo além do CRUD básico proposto.  
A implementação envolveu:
- Criação de uma nova rota no Flask para filtrar tarefas por status;
- Atualização dos testes automatizados para validar o novo comportamento;
- Inclusão da nova feature no quadro Kanban e documentação no README.

Essa mudança demonstra a aplicação prática da **flexibilidade da metodologia ágil**, que permite ajustar o produto conforme as necessidades surgem durante o ciclo de desenvolvimento.

---
---

## Histórico de Commits Semânticos

| Nº | Tipo | Descrição |
|----|------|------------|
| 1 | feat | Criar estrutura inicial do projeto Flask |
| 2 | feat | Adicionar modelo de tarefas (Task) |
| 3 | feat | Implementar CRUD básico de tarefas |
| 4 | refactor | Melhorar organização das rotas e funções |
| 5 | docs | Atualizar README com detalhes do projeto |
| 6 | test | Adicionar testes automatizados com Pytest |
| 7 | chore | Configurar pipeline de integração contínua |
| 8 | fix | Corrigir erro na exclusão de tarefas |
| 9 | feat | Adicionar filtro de tarefas por status (mudança de escopo) |
| 10 | docs | Registrar mudança de escopo no README |

---

## Conclusão

Este projeto demonstra a aplicação prática dos conceitos de **Engenharia de Software Ágil**, incluindo:
- Planejamento e versionamento de código  
- Uso do **Kanban** como ferramenta de organização  
- Implementação de **testes automatizados**  
- Execução de **integração contínua (CI)** com GitHub Actions  

A experiência reforça a importância da modelagem, colaboração e automação no ciclo de vida de um software, mesmo em projetos pequenos.

---


