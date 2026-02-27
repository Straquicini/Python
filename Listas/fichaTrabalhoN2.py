# Ficha de Manipulação de Listas em Python: Gestor de Tarefas

# Cenário

# O formando será responsável por desenvolver um programa que permite ao utilizador
# gerir uma lista de tarefas. O programa deverá suportar as seguintes funcionalidades,
# utilizando os métodos de lista apropriados:

# 1. Adicionar Tarefa: Adicionar uma nova tarefa ao final da lista.
tarefas = ["Estudar python"]
tarefas.append("Estudar SQL")
print(tarefas)

print("\n")
# 2. Adicionar Múltiplas Tarefas: Adicionar várias tarefas de uma vez.
tarefas_adicionais = ["Estudar Front-end", "Estudar JAVA", "Estudar NodeJS"]
tarefas.append("Estudar Front-end")
tarefas.append("Estudar JAVA")
tarefas.append("Estudar NodeJS")
print(tarefas)

print("\n")
# 3. Inserir Tarefa em Posição Específica: Adicionar uma tarefa numa posição específica da lista.
tarefas.insert(2, "Estudar Back-end")
print(tarefas)

print("\n")
# 4. Remover Tarefa por Nome : Remover uma tarefa específica da lista pelo seu conteúdo.
tarefas.remove("Estudar NodeJS")
print(tarefas)

print("\n")
# 5. Remover Última Tarefa ou por Índice: Remover a última tarefa ou uma tarefa numa posição específica.
tarefas.pop(1)
print(tarefas)

print("\n")
# 7. Contar Ocorrências de Tarefa: Verificar quantas vezes uma tarefa específica aparecena lista.
print(tarefas.count("Estudar JAVA"))

print("\n")
# 8. Encontrar Índice de Tarefa: Localizar a primeira ocorrência de uma tarefa na lista.
print(tarefas.index("Estudar Back-end"))

print("\n")
# 9. Ordenar Tarefas: Organizar as tarefas em ordem alfabética.
tarefas.sort()
print(tarefas)

print("\n")
# 10. Inverter Ordem das Tarefas: Reverter a ordem atual das tarefas.
tarefas.reverse()
print(tarefas)

print("\n")
# 11. Copiar Lista de Tarefas: Criar uma cópia independente da lista de tarefas.
tarefas2 = tarefas.copy()
print(tarefas)

print("\n")
# 6. Remover todas as Tarefas: Remover todas as tarefas da lista.
tarefas.clear()
print(tarefas)

print("\n")