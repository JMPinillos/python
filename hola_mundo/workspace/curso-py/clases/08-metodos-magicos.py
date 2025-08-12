class Perro:

    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    # Método mágico "str"
    def __str__(self):
        return f"Clase perro {self.nombre}"

    # Método mágico "destructor" (no suele usarse)
    def __del__(self):
        print(f"{self.nombre} ha sido eliminado")

    def habla(self):
        print(f"Mi nombre es {self.nombre}, Guau!")


perro = Perro("Pachu", 21)
texto = str(perro)
print(texto)
