class Ave:

    def __init__(self):
        self.volador = "volador"

    def vuela(self):
        print("Ave volando")


class Pato(Ave):

    def __init__(self):
        super().__init__()
        self.nada = "nadador"

    def vuela(self):
        print("Pato volando")


pato = Pato()

print(pato.nada, pato.volador)
