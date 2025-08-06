saludo = 25


def saludar():
    global saludo
    saludo = "Hola mundo"
    print(saludo)


def saludaChanchito():
    saludo = 24
    return saludo


result1 = saludo + 3
print(result1)

saludar()

result2 = saludaChanchito() + 3
print(result2)
