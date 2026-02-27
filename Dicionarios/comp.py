# Dicionário em que as chaves vão de 1 a 20 e o valor é a chave 10
d = {n: n+10 for n in range(1,11)}
print(d)
aluno = {'matematica': 12, 'informática': 15, 'português': 17}
notas_maiores_ou_igual_a_15 = {c: v for c, v in aluno.items() if v >= 15}
print(notas_maiores_ou_igual_a_15)

nomes = ["Alicate", "Chave de fenda", "Martelo", "Furadeira"]
dict_nomes = {f: len(f) for f in nomes}