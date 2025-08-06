# lista1 = [1, 2, 3, 4]
# print(lista1)
# print(*lista1)

# tupla = (1, 2, 3, 4)
# print(tupla)
# print(*tupla)

# def n(*nx):
#     print(*nx)


# lista2 = [1, 2, 3, 4, 5]
# n(*lista2)

# lista3 = [5, 6]

# combinada = [*lista1, *lista3]

# combinada = ["hola", *lista1, *lista3, "Pini"]
# print(combinada)

# punto1 = {"x": 19}
# punto2 = {"y": 15}

# nuevo_punto = {**punto1, **punto2}

# print(nuevo_punto)


punto1 = {"x": 19, "y": "pepe"}
punto2 = {"y": 15}

nuevo_punto = {**punto1, **punto2}

print(nuevo_punto)
