class Animal:
    def comer(self):
        print("comiendo")


class Caminante:
    def caminar(self):
        print("Caminando")


class Voldador:
    def volar(self):
        print("Volando")


class Nadador:
    def nadar(self):
        print("Nadando")


class Perro(Caminante, Nadador):
    def saltar(self):
        print("Saltando")


class Pato(Voldador, Caminante, Nadador):
    def programar(self):
        print("Ave programando")


Linda = Perro()
Arquimedes = Pato()

Linda.caminar()
Arquimedes.programar()
