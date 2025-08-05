usuarios = [
    ["Felipe", 4],
    ["Juan", 1],
    ["Pedro", 3]
]

print(usuarios)

# ********** versión 1 *********
# nombres = []

# for usuario in usuarios:
#     nombres.append(usuario[0])

# print(nombres)

# ********** versión 1 optimizada *********
# nombres = [usuario[0] for usuario in usuarios]

# print(nombres)

# ********** versión 2 con filtrado *********
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]

# print(nombres)

# ********** versión 3 con modificación y filtrado *********
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]

print(nombres)
