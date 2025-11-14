import json
import os

def carregar_inventario(ficheiro="inventario.json"):
    """Inventário de um ficheiro JSON."""
    if not os.path.exists(ficheiro):
        return []

    try:
        with open(ficheiro, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, ValueError):
        print("Ficheiro corrompido. Inventário iniciado vazio.")
        return []


def guardar_inventario(inventario, ficheiro="inventario.json"):
    """Guarda o inventário num ficheiro JSON."""
    with open(ficheiro, "w", encoding="utf-8") as f:
        json.dump(inventario, f, indent=4, ensure_ascii=False)

def gerar_id(inventario):
    """Gera um ID único baseado no maior ID existente."""
    if not inventario:
        return 1
    return max(livro["id"] for livro in inventario) + 1


def validar_inteiro(mensagem):
    """Garante que o utilizador insere um número inteiro positivo."""
    while True:
        valor = input(mensagem)
        if valor.isdigit() and int(valor) >= 0:
            return int(valor)
        print("Valor inválido. Introduza um número inteiro positivo.")


def validar_float(mensagem):
    """Garante que o utilizador insere um float positivo."""
    while True:
        valor = input(mensagem)
        try:
            valor = float(valor)
            if valor >= 0:
                return valor
            print("O valor deve ser positivo.")
        except ValueError:
            print("Valor inválido. Introduza um número (ex: 12.50).")


def encontrar_livro(inventario, id_livro):
    """Devolve o livro com o ID indicado, ou None."""
    for livro in inventario:
        if livro["id"] == id_livro:
            return livro
    return None

def ver_inventario(inventario):
    """Mostra todos os itens do inventário."""
    if not inventario:
        print("\nInventário vazio.\n")
        return

    print("\n**INVENTÁRIO**")
    print(f"{'ID':<5} {'TÍTULO':<25} {'AUTOR':<20} {'QTD':<5} {'PREÇO (€)':<10}")
    print("-" * 70)

    for livro in inventario:
        print(f"{livro['id']:<5} {livro['titulo']:<25} {livro['autor']:<20} {livro['quantidade']:<5} {livro['preco']:<10.2f}")

    print("-" * 70 + "\n")


def adicionar_item(inventario):
    """Adiciona um novo livro ao inventário."""
    print("\n=== Adicionar Novo Livro ===")

    titulo = input("Título: ")
    autor = input("Autor: ")
    quantidade = validar_inteiro("Quantidade: ")
    preco = validar_float("Preço (€): ")

    novo_livro = {
        "id": gerar_id(inventario),
        "titulo": titulo,
        "autor": autor,
        "quantidade": quantidade,
        "preco": preco
    }

    inventario.append(novo_livro)
    print("Livro adicionado com sucesso!\n")


def atualizar_quantidade(inventario):
    """Atualiza o stock de um livro existente."""
    print("\n**Atualizar Quantidade**")
    id_livro = validar_inteiro("ID do livro: ")

    livro = encontrar_livro(inventario, id_livro)
    if not livro:
        print("Livro não encontrado.\n")
        return

    nova_qtd = validar_inteiro("Nova quantidade: ")
    livro["quantidade"] = nova_qtd

    print("Quantidade atualizada com sucesso!\n")


def remover_item(inventario):
    """Remove um livro do inventário."""
    print("\n**Remover Livro**")
    id_livro = validar_inteiro("ID do livro a remover: ")

    livro = encontrar_livro(inventario, id_livro)
    if not livro:
        print("Livro não encontrado.\n")
        return

    inventario.remove(livro)
    print("Livro removido com sucesso!\n")


def pesquisa_avancada(inventario):
    """Pesquisa livros por título ou autor."""
    print("\n=== Pesquisa Avançada ===")
    termo = input("Pesquisar por título ou autor: ").lower()

    resultados = [livro for livro in inventario
                  if termo in livro["titulo"].lower() or termo in livro["autor"].lower()]

    if not resultados:
        print("Nenhum resultado encontrado.\n")
        return

    print("\nResultados:")
    for livro in resultados:
        print(f"- {livro['id']} | {livro['titulo']} | {livro['autor']}")
    print()


def relatorio_stock(inventario):
    """Calcula e exibe o valor total do inventário."""
    total = sum(livro["preco"] * livro["quantidade"] for livro in inventario)
    print(f"\nValor total do inventário: {total:.2f} €\n")

def menu():
    inventario = carregar_inventario()

    while True:
        print("""
**MENU PRINCIPAL**

1. Ver Livros
2. Adicionar Livro
3. Atualizar quantidade
4. Remover Livro
5. Pesquisar Livros
6. Stock
7. Guardar e sair

""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ver_inventario(inventario)
        elif opcao == "2":
            adicionar_item(inventario)
        elif opcao == "3":
            atualizar_quantidade(inventario)
        elif opcao == "4":
            remover_item(inventario)
        elif opcao == "5":
            pesquisa_avancada(inventario)
        elif opcao == "6":
            relatorio_stock(inventario)
        elif opcao == "7":
            guardar_inventario(inventario)
            print("\nInventário guardado com sucesso!")
            print("Programa terminado.")
            break
        else:
            print("Escolha inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu()
