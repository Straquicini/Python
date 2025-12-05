class Veiculo:
    total_veiculos = 0
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        Veiculo.total_veiculos += 1
        
    # Getter para marca
    @property
    def marca(self):
        return self.__marca
    
    # Setter para marca
    @marca.setter
    def marca(self, nova_marca):
        if len(nova_marca) < 0:
            print ("Marca inválida")
        self.__marca = nova_marca
        
    # Getter para modelo
    @property
    def modelo(self):
        return self.__modelo
    
    # Setter para modelo
    @modelo.setter
    def modelo(self, novo_modelo):
        if len(novo_modelo) < 0:
            print ("Modelo inválido")
        self.__modelo = novo_modelo
        
    # Getter para ano
    @property
    def ano(self):
        return self.__ano
    
    # Setter para ano
    @ano.setter
    def ano(self, novo_ano):
        if (novo_ano) < 0:
            print ("Ano inválido")
        self.__ano = novo_ano