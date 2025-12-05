from Classes.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca,modelo,ano)
        self.portas = portas
        Veiculo.total_veiculos += 1
                
    # Getter para portas
    @property
    def portas(self):
        return self.__portas
    
    # Setter para portas
    @portas.setter
    def portas(self, nova_porta):
        if (nova_porta) < 0:
            print ("nº portas inválido")
        self.__portas = nova_porta