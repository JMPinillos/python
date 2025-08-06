def es_palindromo(texto):

    # Convertimos el texto a minúsculas y eliminamos espacios
    texto_limpio = texto.lower().replace(" ", "")

    # Invertimos el texto limpio usando slicing
    texto_invertido = texto_limpio[::-1]

    if texto_limpio == texto_invertido:
        return (True)
    else:
        return (False)


print(es_palindromo("Amo la paloma"))
print(es_palindromo("Abba"))
print(es_palindromo("Hola Mundo"))
print(es_palindromo("Reconocer"))
