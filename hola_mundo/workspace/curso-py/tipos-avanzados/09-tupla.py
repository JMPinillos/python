numeros = (1, 2, 3)
print(numeros)

numeros = numeros + (4, 5, 6)
print(numeros)

punto = [1, 2]
print(punto)

punto = tuple([1, 2])
print(punto)


print(numeros[1:3])

primero, segundo, *otros = numeros
print(primero, segundo, otros)

for n in numeros:
    print(n)

numeros = numeros[:3]+(2, 3)
print(numeros)
