class Perro:

    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("Guau!")

    @classmethod
    def factory(cls):
        return cls("Pulgas", 23)

# Perro.habla()


perro1 = Perro("Frida", 8)
perro2 = Perro("Pachu", 13)

# perro1.habla()
perro3 = Perro.factory()
print(perro3.edad, perro3.nombre)
