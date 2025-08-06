import random
random.seed(42)

mascotas = ["Lish", "Pachu", "Frida", "Pulgas"]
numeros_aleatorios = []

for i in range(11):
    numeros_aleatorios.append(random.randint(1, 100))

# print(mascotas)
# print(numeros_aleatorios)

# mascotas.sort()
# numeros_aleatorios.sort()
# print(mascotas)
# print(numeros_aleatorios)

# numeros_aleatorios.sort(reverse=True)
# print(numeros_aleatorios)

# numeros2 = sorted(numeros_aleatorios, reverse=True)
# print(numeros_aleatorios)
# print(numeros2)

usuarios = [
    [4, "Felipe"],
    [1, "Juan"],
    [3, "Pedro"]
]

print(usuarios)

usuarios.sort()
print(usuarios)

usuarios = [
    ["Felipe", 4],
    ["Juan", 1],
    ["Pedro", 3]
]

print(usuarios)

usuarios.sort()
print(usuarios)


def ordena(elemento):
    return elemento[1]


usuarios.sort(key=ordena)
print(usuarios)
