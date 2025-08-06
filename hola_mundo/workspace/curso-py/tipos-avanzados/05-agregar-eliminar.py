mascotas = ["Lish", "Pachu", "Frida", "Pulgas"]

print(mascotas)

mascotas.insert(1, "WiFi")
print(mascotas)

mascotas.append("Lupita")
print(mascotas)

mascotas.append("Frida")
mascotas.append("Frida")
print(mascotas)

mascotas.remove("Frida")
print(mascotas)

mascotas = [mascota for mascota in mascotas if mascota != "Frida"]
print(mascotas)

mascotas.append("Frida")
print(mascotas)

mascotas.pop()
print(mascotas)

mascotas.pop(2)
print(mascotas)

del mascotas[1]
print(mascotas)

mascotas.clear()
print(mascotas)
