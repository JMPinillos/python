class Animal:
    def comer(self):
        print("comiendo")


class Perro(Animal):
    def pasear(self):
        print("Pasenado")

    # def comer(self):
    #     print("comiendo")


class Tortuga(Animal):

    def nadar(self):
        print("Nadando")

    # def comer(self):
    #     print("comiendo")


Linda = Perro()
Lenta = Tortuga()

Linda.comer()
Lenta.nadar()
