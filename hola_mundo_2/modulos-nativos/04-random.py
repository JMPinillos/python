import random
from datetime import datetime

print(random.randint(1, 100))

lista = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(lista)

print(lista)

lista2 = [1, 2, 3, 4, 5, 6, 7, 8]
print(random.choice(lista2))
print(random.choices(lista2, k=3))


# Convertimos la fecha actual a una cadena
fecha_str = datetime.now().strftime("%Y%m%d%H%M%S")

# Creamos el conjunto de caracteres
caracteres = ".,:;abcdefghijklmnopqrstuvwxyz" + fecha_str

# Generamos la cadena aleatoria
cadena = "".join(random.choices(caracteres, k=8))
print(cadena)
print(fecha_str)
