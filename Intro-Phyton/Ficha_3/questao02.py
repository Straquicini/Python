# Escreva uma função chamada contar_caracteres que receba uma string como
# parâmetro e retorne um dicionário onde as chaves são os caracteres da string e os
# valores são o número de vezes que cada caractere aparece.
# Exemplo:

def contar_caracteres(texto):
    d = {}
    for char in texto:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    return d

resultado = contar_caracteres("Monitor")
print(resultado)
