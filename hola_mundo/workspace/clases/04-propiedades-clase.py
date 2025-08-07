class Perro:

    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


Perro.patas = 3
mi_perro = Perro("Pulgas", 15)
mi_perro.patas = 5

print(Perro.patas)
print(mi_perro.patas)

mi_perro_2 = Perro("Frida", 23)
print(mi_perro_2.patas)
