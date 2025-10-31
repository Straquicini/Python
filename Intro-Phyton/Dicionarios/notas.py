notas = {
    'sergio': {'matematica': 13.25, 'programacao': 17.75, 'outras': [12.25, 13.50, 17]},
    'gonçalo': {'matematica': 14.25, 'programacao': 12.50, 'outras': [11.25, 12.50, 8.25]},
    'renan': {'matematica': 16.25, 'programacao': 12.75, 'outras': [8.25, 11.50, 13.25]},
    'tomas': {'matematica': 8.25, 'programacao': 15, 'outras': [10.25, 12.50, 17.75]}
}

# imprimir a nota de matemática do gonçalo
print(notas['gonçalo']['matematica'])

# Imprimir a maior nota de matemática
maior_notaM = 0
for k in notas.keys():
    if notas[k]['matematica'] > maior_notaM:
        maior_notaM = notas[k]['matematica']
print(maior_notaM)

# Imprimir a maior nota de matemática (List Comprehensio)
print(max([notas[k]['matematica'] for k in notas.keys()]))
 
# Nova nota em outas diciilinas para o Tómas
notas['tomas']['outras'].append(6.25)
print("Média da outas disciplinas do Tómas:")
print(f"{sum(notas['tomas']['outras']) / len(notas['tomas']['outras'])}")

# Imprimir o aluno com maior nota de programação
melhor_aluno = 0
maior_nota= 0
for j in notas.keys():
    if notas[j]['programacao'] > maior_nota:
        melhor_aluno = j
print(melhor_aluno)
