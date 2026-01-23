import sqlite3
from tarefa import Tarefa

class GestorBD:
    def __init__(self):
        self.gestor_bd = gestor_bd
        self.criar_tabela()

    def ligar(self):
        return sqlite3.connect(self.gestor_bd)

    def criar_tabela(self):
        conexao = self.ligar()
        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT,
                data_limite TEXT,
                concluida INTEGER
            )
        """)
        conexao.commit()
        conexao.close()

    def adicionar_tarefa(self, tarefa: Tarefa):
        conexao = self.ligar()
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO tarefas (titulo, descricao, data_limite, concluida)
            VALUES (?, ?, ?, ?)
        """, (tarefa.get_titulo(),
              tarefa.get_descricao(),
              tarefa.get_data_limite(),
              tarefa.get_concluida()))
        conexao.commit()
        conexao.close()

    def listar_tarefas(self):
        conexao = self.ligar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM tarefas")
        resultados = cursor.fetchall()
        conexao.close()
        return resultados

    def marcar_concluida(self, id_tarefa):
        conexao = self.ligar()
        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE tarefas
            SET concluida = 1
            WHERE id = ?
        """, (id_tarefa,))
        conexao.commit()
        conexao.close()

    def remover_tarefa(self, id_tarefa):
        conexao = self.ligar()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))
        conexao.commit()
        conexao.close()

        
  
        
