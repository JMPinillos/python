class Lista(list):
    def prepend(self, number: int):
        self.insert(0, number)


lista = Lista([1, 2, 3])

print(lista)

lista.append(4)

print(lista)

lista.prepend(0)

print(lista)
