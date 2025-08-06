print("""¡Bienvenidos a la calculadora!
Para salir escribe Salir.
Las operaciones son suma, multi, div y resta.
""")
# DECLARACIÓN DE VARIABLES
number_1 = number_2 = operator = None

# DEFINICIÓN DE LAS FUNCIONES QUE REALIZAN LAS OPERACIONES
# Función que suma dos números


def suma(a, b):
    return a + b

# Función que resta el segundo número al primero


def resta(a, b):
    return a - b

# Función que multiplica dos números


def multi(a, b):
    return a * b

# Función que divide el primer número entre el segundo
# Incluye una comprobación para evitar división por cero


def div(a, b):
    if b == 0:
        print("No puede dividirse por 0")
    else:
        return a / b


# Función que solicita al usuario un número y valida que sea correcto
def obtener_numero():
    while True:
        try:
            # Intenta convertir la entrada a número decimal
            numero = (input("Introduce un número: "))

            if numero.lower() == "salir":
                exit()
            else:
                return float(numero)  # Si tiene éxito, lo devuelve
        except ValueError:
            # Si falla, muestra un mensaje y repite
            print("¡Error! Debes introducir un número.")

# Función que solicita al usuario un operador válido: ["suma", "multi", "div", "resta"]


def obtener_operador():
    while True:
        operador = input("Introduce un operador: ")  # Solicita el operador

        # Comprueba si el operador está en la lista de permitidos
        if operador.lower() == "salir":
            exit()
        elif operador.lower() in ["suma", "multi", "div", "resta"]:
            return operador  # Si es válido, lo devuelve
        else:
            # Si no, muestra un mensaje y repite
            print("¡Error! Debes introducir un operador.")


# Diccionario que asocia cada operador con su función correspondiente
operaciones = {
    "suma": suma,
    "resta": resta,
    "multi": multi,
    "div": div
}


while True:

    if number_1 is None:
        # Solicita el primer número al usuario
        number_1 = obtener_numero()

        # Solicita el operador al usuario
        operator = obtener_operador()

        # Solicita el segundo número al usuario
        number_2 = obtener_numero()

    else:
        # Solicita el operador al usuario
        operator = obtener_operador()

        # Solicita el segundo número al usuario
        number_2 = obtener_numero()

    # Obtiene la función correspondiente al operador introducido
    calculator = operaciones.get(operator)

    # Ejecuta la función con los dos números como argumentos
    result = calculator(number_1, number_2)

    # Muestra el resultado por pantalla
    print(f"{number_1} {operator} {number_2} = {result}")

    number_1 = result
