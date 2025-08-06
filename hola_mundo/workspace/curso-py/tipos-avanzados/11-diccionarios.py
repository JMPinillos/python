# punto = {"x": 25, "y": 50}
# print(punto)

# print(punto["x"])
# print(punto["y"])

# punto["z"] = 45
# print(punto)

# print(punto.get("x"))
# print(punto.get("lala"))
# print(punto.get("lala", "No existe"))

# del punto["y"]
# print(punto)

# punto["y"] = 50
# print(punto)

# for p in punto:
#     print(p, punto[p])

# for p in punto.items():
#     print(p)

# ********** Uso real *********
usuarios = [
    {"id": 1, "name": "Pepe"},
    {"id": 2, "name": "Juan"},
    {"id": 3, "name": "Ana"},
    {"id": 4, "name": "Pini"}
]

for usuario in usuarios:
    print(usuario["name"])

# ********** Uso real avanzado*********
# ids = [1, 2, 3, 4]
# names = "Pepe", "Pini", "Ana", "Juan"
# users = []

# for id, name in zip(ids, names):
#     users.append({"id": id, "name": name})

# print(users)
