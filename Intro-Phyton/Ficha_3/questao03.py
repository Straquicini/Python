biblioteca = {
    "livro1": {
        "titulo": "Python Fluente",
        "autor": "Luciano Ramalho",
        "ano": 2015,
        "disponivel": True
    },
    "livro2": {
        "titulo": "Pense em Python",
        "autor": "Allen B. Downey",
        "ano": 2012,
        "disponivel": False
    },
    "livro3": {
        "titulo": "Introdução à Programação com Python",
        "autor": "Nilo Ney Coutinho Menezes",
        "ano": 2019,
        "disponivel": True
    }
}

# 1. Imprimir os títulos de todos os livros disponíveis
print("Livros disponiveis:")
for livro in biblioteca.values():
    if livro["disponivel"]:
        print(livro["titulo"])
        
# 2. Adicionar um novo livro à biblioteca
biblioteca["livro4"] = {
        "titulo": "Programação com Java Avançada",
        "autor": "Charles saraiva",
        "ano": 2020,
        "disponivel": False
}

# 3. Marcar o "lirvro1" como não disponível
biblioteca["livro1"]["disponivel"] = False
#print(biblioteca["livro1"])

# 4. Criar uma função que retorne uma lista com os títulos dos livros de um determinado autor
def livros_do_autor(autor):
    livros_do_autor = []
    for livro in biblioteca.values():
        if livro['autor'] == autor:
            livros_do_autor.append(livro['titulo'])
    return livros_do_autor