from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulação de banco de dados em memória
tarefas = []
id_counter = 1

@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas)

@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    global id_counter
    dados = request.json
    nova_tarefa = {
        "id": id_counter,
        "titulo": dados["titulo"],
        "descricao": dados.get("descricao", ""),
        "prioridade": dados.get("prioridade", "normal")
    }
    tarefas.append(nova_tarefa)
    id_counter += 1
    return jsonify(nova_tarefa), 201

@app.route("/tarefas/<int:id_tarefa>", methods=["PUT"])
def atualizar_tarefa(id_tarefa):
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            dados = request.json
            tarefa["titulo"] = dados.get("titulo", tarefa["titulo"])
            tarefa["descricao"] = dados.get("descricao", tarefa["descricao"])
            tarefa["prioridade"] = dados.get("prioridade", tarefa["prioridade"])
            return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada"}), 404

@app.route("/tarefas/<int:id_tarefa>", methods=["DELETE"])
def deletar_tarefa(id_tarefa):
    global tarefas
    tarefas = [t for t in tarefas if t["id"] != id_tarefa]
    return jsonify({"mensagem": "Tarefa removida com sucesso"})

if __name__ == "__main__":
    app.run(debug=True)
