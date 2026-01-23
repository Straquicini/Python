from tarefa import Tarefa
from gestor_da_bd import GestorBD

def mostrar_menu():
    print("\n--- Gestor de Tarefas ---")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("0. Sair")

def adicionar_tarefa(gestor):
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    data_limite = input("Data limite (YYYY-MM-DD): ")
    tarefa = Tarefa(titulo, descricao, data_limite)
    gestor.adicionar_tarefa(tarefa)
    print("Tarefa adicionada com sucesso.")

def listar_tarefas(gestor):
    tarefas = gestor.listar_tarefas()
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return

    for t in tarefas:
        estado = "Concluída" if t[4] == 1 else "Pendente"
        print(f"ID: {t[0]}")
        print(f"Título: {t[1]}")
        print(f"Descrição: {t[2]}")
        print(f"Data Limite: {t[3]}")
        print(f"Estado: {estado}")
        print("-" * 30)

def marcar_concluida(gestor):
    id_tarefa = int(input("ID da tarefa a marcar como concluída: "))
    gestor.marcar_concluida(id_tarefa)
    print("Tarefa marcada como concluída.")

def remover_tarefa(gestor):
    id_tarefa = int(input("ID da tarefa a remover: "))
    gestor.remover_tarefa(id_tarefa)
    print("Tarefa removida com sucesso.")

def main():
    gestor = GestorBD()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa(gestor)
        elif opcao == "2":
            listar_tarefas(gestor)
        elif opcao == "3":
            marcar_concluida(gestor)
        elif opcao == "4":
            remover_tarefa(gestor)
        elif opcao == "0":
            print("A sair da aplicação.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
