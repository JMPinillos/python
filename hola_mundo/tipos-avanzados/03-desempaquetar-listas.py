# numeros = [1, 2, 3]
numeros = list(range(1, 10))
# primero, segundo, tercero = numeros
# primero, *otros = numeros

primero, *otros, ultimo = numeros

print(primero, otros, ultimo)
