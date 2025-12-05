from Classes.veiculo import Veiculo     
from Classes.carro import Carro    
from Classes.moto import Moto
                
# Área de teste
v1 = Veiculo("BMW", "m2", 2020)
v2 = Veiculo("BMW", "m3", 2021)
v3 = Veiculo("BMW", "m4", 2022)
c1 = Carro("BMW", "m4", 2022, 4)
m1 = Moto("BMW", "m4", 2022, 125)

print(Veiculo.total_veiculos)
print(c1.portas)
print(m1.cilindrada)