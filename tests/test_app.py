import json
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import app


def test_criar_tarefa():
    cliente = app.test_client()
    resposta = cliente.post("/tarefas", json={
        "titulo": "Estudar Engenharia de Software",
        "descricao": "Ler capítulo 4 do livro",
        "prioridade": "alta"
    })
    assert resposta.status_code == 201
    dados = resposta.get_json()
    assert dados["titulo"] == "Estudar Engenharia de Software"
