# Exercio 01
# Crie um programa que peça o comprimento e a largura
# de um retângulo e mostre a área e o perimetro

# Exercicio 02
# Crie uma lista comm 10 números e imprima apenas os números pare

# Exercicio 03
# Crie um dicionário em que as chaves sejam nomes de produtos.
# Os valores sejam o preço de cada produto.
# Deve devolver o produto mais caro e a média dos preços.

# Exercicio 01

print('\n')
comp = float(input("Digite o comprimento do retângulo: "))
area = float(input("Digite o área do retângulo: "))

print(f'O comprimento do retângulo é {comp} e a área é {area}')
print('\n')

# Exercicio 02

print('\n')
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for pares in nums:
    if pares % 2 == 0:
        print(pares)
print('\n')

# Exercicio 03

print('\n')
produtos = {"Rato": 10, "Teclado": 20, "Monitor": 100}

print(produtos)

print('\n')

for nome in produtos.keys():
    print(nome)
for preco in produtos.values():
    print(preco)

print('\n')

soma = 0
precoMaisCaro = 0
produtoMaisCaro = ""
    
for p, v in produtos.items():
    soma =+ preco
    if preco > precoMaisCaro:
        precoMaisCaro = preco
        produtoMaisCaro = p

media = soma / len(produtos)

print(f'O produto mais caro é {produtoMaisCaro}')
print(f'A média dos valores {media:.2f}')
print('\n')


    