class Perro:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Guau!")

    def cambio_nombre(self, nombre):
        self.nombre = nombre
        print(f"Mi nuevo nombre es {self.nombre}")


mi_perro = Perro("Pulgas", 15)
mi_perro.habla()
mi_perro.cambio_nombre("Frida")
mi_perro.habla()
