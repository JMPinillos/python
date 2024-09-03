# triangulo.py
from IForma import Forma

class Triangulo(Forma):
    def area(self):
        return (self.base * self.altura) / 2
