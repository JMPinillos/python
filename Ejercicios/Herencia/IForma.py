from abc import ABC, abstractmethod

class Forma(ABC):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        pass