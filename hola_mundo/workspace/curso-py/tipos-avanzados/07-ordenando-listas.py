usuarios = [
    ["Felipe", 4],
    ["Juan", 1],
    ["Pedro", 3]
]

print(usuarios)

usuarios.sort(key=lambda el: el[1])
print(usuarios)
