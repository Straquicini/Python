from math import sqrt
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        
    def formarTriangulo(self):
        c1 = self.lado1 > self.lado2+self.lado3
        c2 = self.lado2 > self.lado1+self.lado3
        c3 = self.lado3 > self.lado1+self.lado2
        return c1 and c2 and c3
        
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
    def area(self):
        p = self.perimetro() / 2
        return sqrt(p * (p-self.lado1) * (p-self.lado2) * (p-self.lado3))
    
    def tipo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return 'Equilátero'
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return 'Isósceles'
        return 'Escaleno'
    
class Retangulo:
    def __init__(self, lado1, lado2, cor):
        self.lado1 = lado1
        self.lado2 = lado2
        self.cor = cor
        
    def quadrado(self):
        return self.lado1 ==self.lado2
    
    def diagonal(self):
        return sqrt(pow(self.lado1, 2) + pow(self.lado2, 2))
    
    def perimetro(self):
        return 2 * self.lado1 + 2 * self.lado2
    
    def mesmoPerimetro(self, rect):
        if not isinstance(rect, Retangulo):
            return False
        return self.perimetro() == rect.perimetro()
    
    def mesmaCor(self, rect):
        if not isinstance(rect, Retangulo):
            return False
        return self.cor == rect.cor
    
class ComandoTv:
    def __init__(self, marca, anoFabrico, canal, volume, ligado = False):
        self.marca = marca
        self.anoFrabico = anoFabrico
        self.__canal = canal
        self.__volume = volume
        self.ligado = ligado
        
    # Getter para canal
    @property
    def canal(self, novo_canal):
        return self.__canal
    
    # Setter para canal
    @canal.setter
    def canal(self, novo_canal):
        if novo_canal < 100:
            print("Canal inválido")
        else: self.__canal = novo_canal
        
    # Getter para volume
    @property
    def volume(self, novo_volume):
        return self.__volume
    
    # Setter para volume
    @volume.setter
    def volume(self, novo_volume):
        if novo_volume < 50:
            print("Volume inválido")
        else: self.__volume = novo_volume
        
    def trocarCanal(self, canal):
        if canal<100 and canal>0: return canal
        else: return self.canal
        
    def alterarVolume(self, sinal):
        if sinal == "+":
            if self.volume < 50: return self.volume+1
        elif sinal == "-" and self.volume > 0:
            return self.volume-1
        return self.volume
    
    def mute(self):
        self.volume = 0
        return self.volume
    
    def ligar(self):
        if self.ligado:
            return False
        return True
        
# TESTE DO COMANDO
c1 = ComandoTv("LG", 2020, 15, 10)

    
# TESTE DO SISTEMA
t = Triangulo(10, 15, 11)
if t.formarTriangulo():
    print(f"Perímetro : {t.perimetro()}")
    print(f"Área: {t.area():.2f}")
    print(t.tipo())
    
r1 = Retangulo(10, 4, "azul")
r2 = Retangulo(6, 8, "verde")
print(r1.mesmoPerimetro(r2))

        