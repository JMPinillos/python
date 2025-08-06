texto = "Hola mundo este es mi string"
lista = []


def text2list(text):
    return ([*text.replace(" ", "")])


lista = text2list(texto)
print(lista)
