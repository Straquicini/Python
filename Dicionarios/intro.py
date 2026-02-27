import os

# aluno = {
#     'nome': 'Renan Straquicini',
#     'naturalidade': 'Brasil',
#     'peso': 62,
#     'altura': 1.72,
#     'aprovado': True
# }

# # Imprimir uma chave do dicionário
# print(aluno['naturalidade'])
# print(f"o aluno {aluno['nome']} tem peso {aluno['peso']}kg.")

# # Características do aluno
# for chave in aluno.keys(): print(chave)
# # Valores das chaves
# for v in aluno.values(): print(v)
# #par chave/valor
# for k, v in aluno.items():
#     print(f"{k}: {v}")
    
# aluno['imc'] = round(aluno['peso'] / (aluno['altura'] * aluno['altura']),2)
# aluno['naturalidade'] = 'Portugal'
# os.system("cls")
# print(aluno)

d = { }
d = dict() # Dicionario vazio
d1 = dict (nome="Marcelo", idade= 50)
d2 = {'nome':'marcelo', 'idade': 50}
#d = dict(('nome', 'marcelo'), ('idade', 50))

d1['idade'] = 51
idade = d1.get('idade2', 'idade desconhecida')
print (idade)

for chave in d2.keys():
    print(chave) # nome, idade
for v in d2.values():
    print(v)  #Macelo, 50
for c, v in d2.items():
    print(f"{c} com valor {v}")
    
produtos = {
    'casaco': {'preco': 23.99, 'iva': 0.23},
    'camisa': {'preco': 71.99, 'iva': 0.13},
    'sapato': {'preco': 55.99, 'iva': 0.23}
}

print(produtos(sorted(produtos.items(), key=lambda item: item[1])))