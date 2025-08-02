# 📝 Sistema de Gerenciamento de Tarefas

Este projeto foi desenvolvido como parte da disciplina de Engenharia de Software, simulando a criação de um sistema ágil para uma startup fictícia chamada **TechFlow Solutions**. O objetivo é permitir o acompanhamento em tempo real de tarefas, priorização e controle de qualidade via integração contínua.

---

## 📌 Objetivo do Projeto

Desenvolver um sistema básico de gerenciamento de tarefas com foco em metodologias ágeis, testes automatizados e documentação técnica.

---

## 🧠 Escopo e Funcionalidades

- ✅ CRUD de Tarefas (Create, Read, Update, Delete)
- ✅ Campo de **prioridade** (baixa, média, alta)
- ✅ Testes automatizados com Pytest
- ✅ Integração contínua com GitHub Actions
- ✅ Kanban no GitHub Projects
- ✅ Simulação de mudança de escopo
- ✅ Modelagem UML

---

## 🚀 Tecnologias Utilizadas

- Python 3.10+
- Flask
- Pytest
- GitHub Actions
- draw.io (para modelagem UML)

---

## 🛠️ Como Executar o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/igor-rgomes/sistema-gerenciamento-tarefas.git
cd sistema-gerenciamento-tarefas
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute o sistema:
```bash
python src/app.py
```

5. Teste a API com Postman ou Insomnia usando as rotas:

- GET /tarefas
- POST /tarefas
- PUT /tarefas/<id>
- DELETE /tarefas/<id>

---

## 🧪 Testes Automatizados

Execute:
```bash
pytest tests/
```
O projeto está integrado ao GitHub Actions, que roda os testes automaticamente a cada push ou pull request.

---

## 🔁 Simulação de Mudança no Escopo

Durante o desenvolvimento, foi identificada a necessidade de priorizar tarefas. Com isso, adicionamos o campo prioridade ao modelo de tarefa e atualizamos:

- Código da API (app.py)
- Testes (test_app.py)
- Documentação
- Quadro Kanban

---

## 🧩 Kanban no GitHub Projects

O fluxo de trabalho foi gerenciado com um quadro Kanban dividido em:

- A Fazer
- Em Progresso
- Concluído

---

## 📐 Modelagem UML

Os seguintes diagramas foram criados com draw.io e estão na pasta docs/uml:

✅ Diagrama de Casos de Uso
✅ Diagrama de Classes
