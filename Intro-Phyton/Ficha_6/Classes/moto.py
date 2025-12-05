from Classes.veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindrada):
        super().__init__(marca,modelo,ano)
        self.cilindrada = cilindrada
        Veiculo.total_veiculos += 1
                
    # Getter para cilindrada
    @property
    def cilindrada(self):
        return self.__cilindrada
    
    # Setter para cilindrada
    @cilindrada.setter
    def cilindrada(self, nova_cilindrada):
        if (nova_cilindrada) < 0:
            print ("cilindrada inválida")
        self.__cilindrada = nova_cilindrada