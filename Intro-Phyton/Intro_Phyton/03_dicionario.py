idade_alunos = {"Rui": 17, "Ana": 19, "Carlos": 21}
#imprimir dicionario
print(idade_alunos)
# Imprimir chaves do dicionario
for nome in idade_alunos.keys():
    print(nome)
# Imprimir valores
for idade in idade_alunos.values():
    print(idade)
    
# Imprimir chaves e valores formatados
for k, v in idade_alunos.itens():
    print(f'O(A) aluno(a) {k} tem {v} anos.')
    
