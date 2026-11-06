import sqlite3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "API SQLite"


@app.route("/tarefas")
def listar_tarefas():
    
    conexao = sqlite3.connect("tarefas.db")
    
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM tarefas")
    
    tarefas_banco = cursor.fetchall()
    
    conexao.close()
    
    tarefas = []
    
    for tarefa in tarefas_banco:
        
        tarefas.append({
            "id": tarefa[0],
            "titulo": tarefa[1],
            "concluida": bool(tarefa[2])
            
        })
    
    return tarefas    

@app.route("/adicionar")
def adicionar():
    
    return {
        "mensagem": "Tarefa adicionada com sucesso!"
    }
    
    
@app.route("/remover/<int:id>")
def remover(id):
    
    conexao = sqlite3.connect("tarefas.db")
    
    cursor = conexao.cursor()
    
    cursor.execute(
        "DELETE FROM tarefas WHERE id = ?",
        (id,)
    )
        
    conexao.commit()
    
    conexao.close()
    
    return {
        "mensagem": "Tarefa removida com sucesso!"
    }
    
    
app.run()
