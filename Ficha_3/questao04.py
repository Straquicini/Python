# Utilize compreensão de dicionários para resolver os seguintes problemas:

# 1. Crie um dicionário onde as chaves são números de 1 a 10 e os valores são os quadrados desses números.
nums_ao_quadrados = {q: q**2 for q in range (1,11)}

# 2. A partir de uma lista de palavras, crie um dicionário onde as chaves são as palavras e os valores são os comprimentos dessas palavras.
palavras = ["C++", "Java", "Python"]
comprimento = {palavras: len(palavras) for palavras in palavras}
print(f"O comprimento da palvra é {comprimento}")

# 3. A partir do dicionário notas = {"Ana": 18, "Bruno": 15, "Carla": 17,"David": 12, "Eva": 19} , crie um novo dicionário que contenha apenas 
# os alunos com notas superiores ou iguais a 15.
notas = {"Ana": 18, "Bruno": 15, "Carla": 17,"David": 12, "Eva": 19}
aluno = {aluno: n for aluno, n in notas.items() if n >= 15}
print(f"Alunos co notas maior ou igual que 15 {aluno}")