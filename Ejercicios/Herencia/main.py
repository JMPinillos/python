from Cuadrado import Cuadrado
from Triangulo import Triangulo

def main():
    cuadrado = Cuadrado(2, 4)
    triangulo = Triangulo(2, 4)

    print(f"Área del rectángulo: {cuadrado.area()}")
    print(f"Área del triángulo: {triangulo.area()}")

if __name__ == "__main__":
    main()