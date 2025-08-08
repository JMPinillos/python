class Perro:
    def __init__(self, nombre: str):
        self.nombre = (nombre)

    @property
    def nombre(self):
        print("pasando por el getter")
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        print("pasando por el setter")
        if nombre.strip():
            self.__nombre = nombre
        return nombre


perro = Perro("Pachu")
print(perro.nombre)
