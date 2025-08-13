from io import open

# ESCRITURA
# texto = "hola mundo"
# archivo = open("archivos/hola-mundo.txt", "w")

# archivo.write(texto)

# archivo.close()

# LECTURA
# archivo = open("archivos/hola-mundo.txt", "r")

# texto = archivo.read()
# archivo.close()
# print(texto)

archivo = open("archivos/hola-mundo.txt", "r")
texto = archivo.readlines()
archivo.close()
print(texto)
