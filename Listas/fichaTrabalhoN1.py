# Crie uma lista com os números pares de 1 a 10.
lista_pares = [i for i in range(1, 11) if i % 2 == 0]
print(lista_pares)

print("\n")
# Crie uma lista com os quadrados dos números de 1 a 10.
quadrados = [i**2 for i in range(1, 11)]
print(quadrados)

print("\n")
# Dada uma lista de palavras, crie uma nova lista que indique o tamanho de cada palavra.
palavras = ["Ana", "Rui", "João", "Marina", "ALice", "Luana"]
palavras_tamanho = [len(i) for i in palavras]
print(palavras_tamanho)

print("\n")
# Dada uma lista de números, crie uma lista apenas com os números maiores que 5.
lista = []
for i in range(1,11):
    lista.append(i)

maior_que_5 = [i for i in lista if i > 5]
print(maior_que_5)

print("\n")
# Crie uma lista com as letras maiúsculas de uma string. (nome = 'MarcelO ViEiRa amorIM')
nome = 'MarcelO ViEiRa amorIM'
maiuscula = [letra for letra in nome if letra.isupper()]
print(maiuscula)

print("\n")
# Dada uma lista de números, crie uma nova lista onde se o número for múltiplo de 3, é apresentado o dobro deste caso contrário aparece o mesmo número da lista original.
lista = []
for i in range(1,11):
    lista.append(i)
    
multiplos_de_3 = [i*2 if i % 3 == 0 else i for i in lista]
print(multiplos_de_3)

print("\n")
# Dada uma lista de nomes, crie uma nova lista apenas com os nomes que começam com a letra "A". Todos os nomes da nova lista devem aparecer em maiúsculas.
nomes = ["Ana", "Rui", "João", "Marina", "ALice", "Luana"]
nome_A = [nome.upper() for nome in nomes if nome.startswith('A')]
print(nome_A)

print("\n")
# Dada uma lista de frutas, crie uma nova lista com o comprimento de cada fruta, apenas para as frutas com mais de 5 letras. Caso contrário, deve aparecer 0.

frutas = ["Pera", "Banana", "Maça", "Melão", "Melancia"]
nova_lista = [len(fruta) if len(fruta) > 5 else 0 for fruta in frutas]
print(nova_lista)