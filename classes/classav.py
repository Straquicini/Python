class Pessoa:
    total_pessoas = 0
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        Pessoa.total_pessoas += 1
    
    def __str__(self):
        return f"{self.__nome} tem {self.__idade} anos"
    
    # Getter para o nome da pessoa
    @property
    def nome(self, novo_nome):
        return self.__nome
    
    # Setter para nome
    @nome.setter
    def nome(self, novo_nome):
        if len(novo_nome) < 2:
            print("Nome inválido")
        else: self.__nome = novo_nome
        
    # Getter para a idade da pessoa
    @property
    def idade(self, nova_idade):
        return self.__idade
    
    # Setter para idade
    @idade.setter
    def idade(self, nova_idade):
        if nova_idade < 0:
            print("Idade inválido")
        else: self.__idade = nova_idade


# Área de teste
p1 = Pessoa("Marcelo", 52)
p2 = Pessoa("Sérgio", 19)
p3 = Pessoa("Tomás", 18)

print(Pessoa.total_pessoas)
print(p2)