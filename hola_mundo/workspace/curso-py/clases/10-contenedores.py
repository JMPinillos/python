class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre} - Precio: {self.precio}"

    def __eq__(self, otro):
        return self.nombre == otro.nombre and self.precio == otro.precio


class Categoria:
    productos = []

    def __init__(self, nombre: str, productos):
        self.nombre = nombre
        self.productos = productos

    def agregar(self, producto):
        if producto in self.productos:
            print(f"{producto.nombre} ya existe en la categoría")
        else:
            self.productos.append(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)


p1 = Producto("Kayak", 1000)
p2 = Producto("Bicicleta", 750)
p3 = Producto("Bicicleta", 500)
p4 = Producto("Bicicleta", 500)

deportes = Categoria("Deportes", [p1, p2])

deportes.imprimir()
print("--------------------")
deportes.agregar(p3)
deportes.imprimir()
print("--------------------")
deportes.agregar(p4)
deportes.imprimir()
