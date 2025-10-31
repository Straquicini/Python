# Exercício 1: Criação e Manipulação Básica
# Crie um dicionário chamado aluno que contenha as seguintes informações: - Nome:
# "Ana Silva" - Idade: 17 - Disciplinas: ["Matemática", "Física", "Informática"] - Notas:
# {"Matemática": 18, "Física": 17, "Informática": 19}
# Em seguida:
# 1. Adicione uma nova disciplina "Português" com nota 16.
# 2. Modifique a idade para 18.
# 3. Imprima todas as disciplinas e respetivas notas.
# 4. Calcule e imprima a média das notas.

aluno = {"Nome": "Ana Silva", "Idade": 17, "Disciplinas": ["Matemática", "Física", "Informática"], "Notas": {"Matemática": 18, "Física": 17, "Informática": 19}}

# 1. Adicionar a disciplina "Português" com nota 16
aluno["Disciplinas"].append("Português")
aluno["Notas"]["Português"] = 16

#2. Modificar a idade para 18
aluno["Idade"] = 18

#3. Imprimir todas as disciplinas e respetivas notas
print("Disciplinas e Notas:")
for disciplina in aluno["Disciplinas"]:
    nota = aluno["Notas"].get(disciplina)
    print(f"{disciplina}: {nota}")

#4. Calcular e imprimir a média das notas
somaNotas = sum(aluno["Notas"].values())
quantidadeDisciplinas = len(aluno["Notas"])
media = somaNotas / quantidadeDisciplinas
print(f"Média final = {media:.2f} valores")