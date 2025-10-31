# Exercício 7: Análise de Texto

# Ler o texto do utilizador
texto = input("Digite um texto: ")

#  Conta a frequência de cada palavra no texto (ignorando maiúsculas/minúsculas e pontuação)
pontuacoes = ".,;:"
for pontuacao in pontuacoes:
    texto = texto.replace(pontuacao, '')

# Separar o texto em palavras
palavras = texto.split()

# Conta frequência das palavras 
frequencia = {}

for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

# Calcular estatísticas básicas
total_palavras = len(palavras)
palavras_unicas = len(frequencia)
soma_tamanhos = 0

for palavra in palavras:
    soma_tamanhos += len(palavra)

comprimento_medio = soma_tamanhos / total_palavras if total_palavras > 0 else 0

# Identifica as 5 palavras mais comuns
# ordena por frequência (maior primeiro)
palavras_ordenadas = sorted(frequencia.items(), key=lambda x: x[1], reverse=True)
cinco_mais_comuns = palavras_ordenadas[:5]

# Monta o dicionário de resultados
resultado = {
    "total_palavras": total_palavras,
    "palavras_unicas": palavras_unicas,
    "comprimento_medio": comprimento_medio,
    "cinco_mais_comuns": cinco_mais_comuns,
    "frequencia_completa": frequencia
}

# Imprimi o resultado
print("\n***Análise do Texto***")
print(f"Total de palavras: {resultado['total_palavras']}")
print(f"Palavras únicas: {resultado['palavras_unicas']}")
print(f"Comprimento médio das palavras: {resultado['comprimento_medio']:.2f}")
print("\n5 palavras mais comuns:")
for palavra, freq in resultado["cinco_mais_comuns"]:
    print(f"  {palavra}: {freq}")

print("\n***Frequência completa***")
for palavra, freq in resultado["frequencia_completa"].items():
    print(f"{palavra}: {freq}")
