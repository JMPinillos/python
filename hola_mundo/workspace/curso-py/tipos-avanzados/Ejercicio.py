from collections import Counter
texto = "Hola mundo este es mi string"

# ********** Parte 1 *********
lista = []


def text2list(text):
    return ([*text.replace(" ", "")])


lista = text2list(texto)
# print(lista)

# ********** Parte 2 *********
# ********** Con una función *********
diccionario = {}


def dic_count(text):
    for char in text:
        if char in diccionario:
            diccionario[char] += 1
        else:
            diccionario[char] = 1


dic_count(lista)
print(diccionario)

# ********** Con una librería *********
# diccionario2 = Counter(texto.replace(" ", ""))
# print(diccionario2)

# ********** Parte 3 *********
lista_tuplas = []


def dic2tuplas(diccionario):
    lista = []
    diccionario_ordenado = sorted(
        diccionario.items(), key=lambda item: item[1], reverse=True)

    for char, count in diccionario_ordenado:
        lista.append((char, count))

    return lista


lista_tuplas = dic2tuplas(diccionario)
print(lista_tuplas)
