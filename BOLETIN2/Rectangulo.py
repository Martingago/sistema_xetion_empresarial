class Rectangulo:
    def __init__(self, altura, base) :
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return (self.base *2) + (self.altura *2)
    
mi_rectangulo = Rectangulo(5,3)
print("area del rectangulo",  mi_rectangulo.calcular_area())
print("perimetro del rectangulo", mi_rectangulo.calcular_perimetro())
    


