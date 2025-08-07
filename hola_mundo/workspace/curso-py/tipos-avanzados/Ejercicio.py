from pprint import pprint

texto = "Hola mundo este es mi string"


# 1 - FUNCIÓN PARA CREAR LISTA SIN ESPACIOS
def text2list(text):
    return ([*text.replace(" ", "")])


# 2 -  FUNCIÓN PARA CREAR DICCIONARIO


def dic_count(lista):
    charts_dict = {}

    for char in lista:
        if char in charts_dict:
            charts_dict[char] += 1
        else:
            charts_dict[char] = 1

    return charts_dict


# 3 - FUNCIÓN PARA OBTENER TUPLAS DE UN DICCIONARIO


def ordena_dic(diccionario):
    return sorted(
        diccionario.items(),
        key=lambda item: item[1],
        reverse=True
    )


# 4 - FUNCIÓN PARA DEVOLVER LAS TUPLAS DE MAYOR VALOR


def mayores_tuplas(tuplas):
    mayor_valor = 0
    respuesta = []

    for char in tuplas:

        if char[1] > mayor_valor:
            mayor_valor = char[1]

    for char in tuplas:

        if char[1] == mayor_valor:
            respuesta.append(char)

    return respuesta

# 5 - FUNCIÓN PARA IMPRIMIR MENSAJE CON LISTAS DE LOS VALORES MÁS REPETIDOS


def mensaje(mayores):
    print("Los caracteres que mas se repiten son:")
    for mayor in mayores:
        print(f"- {mayor[0].upper()} con {mayor[1]} repeticiones")


# 6 - UNA FUNCIÓN PARA LLAMAR A TODAS ;)


def main(text):
    lista = text2list(text)
    diccionario = dic_count(lista)
    lista_tuplas = ordena_dic(diccionario)
    mensaje(mayores_tuplas(lista_tuplas))


# EJECUCIÓN FDE FUNCIONALIDADES PASO A PASO
# lista = text2list(texto)
# print("Lista sin espacios: ", lista)

# diccionario = dic_count(lista)
# print("Diccionario de caracteres contados:")
# pprint(diccionario)

# lista_tuplas = ordena_dic(diccionario)
# print("Lista de tuplas ordenadas por valor descendente:")
# pprint(lista_tuplas)

# mayores = mayores_tuplas(lista_tuplas)
# mensaje(mayores)


# EJECUCIÓN FINAL
main(texto)
