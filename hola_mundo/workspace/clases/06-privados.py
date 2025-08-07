class Perro:

    patas = 4

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.__nombre} dice: Guau!")

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def __metodo_privado(self):
        print("Accediste a un método privado")

    @classmethod
    def factory(cls):
        return cls("Pulgas", 23)


perro1 = Perro.factory()
perro1.habla()

print(perro1.get_nombre())

perro1.set_nombre("frida")
print(perro1.get_nombre())

print(perro1.__dict__)

print(perro1._Perro__nombre)

perro1._Perro__metodo_privado()
