'''Elabore un algoritmo por medio de diagrama de clases, el programa debe recibir información de medidas de cualquier figura geométricas: Triangulo, Circunferencia, Cuadrado, Rectángulo, Paralelogramo, trapecio y rombos. Realice el diagrama de clases representando los objetos y métodos que va implementar para solucionar la situación. Al final el programa debe imprimir el área y perímetro de las figuras.'''

import math

class FiguraGeometrica:
    def area(self):
        pass

    def perimetro(self):
        pass

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

class Circunferencia(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

class Rectangulo(FiguraGeometrica):
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho

    def perimetro(self):
        return 2 * (self.largo + self.ancho)

class Paralelogramo(FiguraGeometrica):
    def __init__(self, base, altura, lado):
        self.base = base
        self.altura = altura
        self.lado = lado

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.lado)

class Trapecio(FiguraGeometrica):
    def __init__(self, base_mayor, base_menor, altura, lado1, lado2):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def area(self):
        return ((self.base_mayor + self.base_menor) * self.altura) / 2

    def perimetro(self):
        return self.base_mayor + self.base_menor + self.lado1 + self.lado2

class Rombo(FiguraGeometrica):
    def __init__(self, diagonal_mayor, diagonal_menor, lado):
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor
        self.lado = lado

    def area(self):
        return (self.diagonal_mayor * self.diagonal_menor) / 2

    def perimetro(self):
        return 4 * self.lado

def menu():
    while True:
        print("\nMenú de Figuras Geométricas: \n")
        print("1. Triángulo")
        print("2. Circunferencia")
        print("3. Cuadrado")
        print("4. Rectángulo")
        print("5. Paralelogramo")
        print("6. Trapecio")
        print("7. Rombo")
        print("8. Salir")
        opcion = input("\nSeleccione una opción: ")
        print("")
        print("-" * 30)
        print("")

        if opcion == "1":
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            lado1 = float(input("Ingrese el primer lado del triángulo: "))
            lado2 = float(input("Ingrese el segundo lado del triángulo: "))
            lado3 = float(input("Ingrese el tercer lado del triángulo: "))
            triangulo = Triangulo(base, altura, lado1, lado2, lado3)
            imprimir_resultados(triangulo)

        elif opcion == "2":
            radio = float(input("Ingrese el radio de la circunferencia: "))
            circunferencia = Circunferencia(radio)
            imprimir_resultados(circunferencia)

        elif opcion == "3":
            lado = float(input("Ingrese el lado del cuadrado: "))
            cuadrado = Cuadrado(lado)
            imprimir_resultados(cuadrado)

        elif opcion == "4":
            largo = float(input("Ingrese el largo del rectángulo: "))
            ancho = float(input("Ingrese el ancho del rectángulo: "))
            rectangulo = Rectangulo(largo, ancho)
            imprimir_resultados(rectangulo)

        elif opcion == "5":
            base = float(input("Ingrese la base del paralelogramo: "))
            altura = float(input("Ingrese la altura del paralelogramo: "))
            lado = float(input("Ingrese el lado del paralelogramo: "))
            paralelogramo = Paralelogramo(base, altura, lado)
            imprimir_resultados(paralelogramo)

        elif opcion == "6":
            base_mayor = float(input("Ingrese la base mayor del trapecio: "))
            base_menor = float(input("Ingrese la base menor del trapecio: "))
            altura = float(input("Ingrese la altura del trapecio: "))
            lado1 = float(input("Ingrese el primer lado del trapecio: "))
            lado2 = float(input("Ingrese el segundo lado del trapecio: "))
            trapecio = Trapecio(base_mayor, base_menor, altura, lado1, lado2)
            imprimir_resultados(trapecio)

        elif opcion == "7":
            diagonal_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
            diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))
            lado = float(input("Ingrese el lado del rombo: "))
            rombo = Rombo(diagonal_mayor, diagonal_menor, lado)
            imprimir_resultados(rombo)

        elif opcion == "8":
            print("Saliendo del programa...")
            exit()

        else:
            print("Opción no válida. Por favor seleccione una opción entre 1 y 8.")

def imprimir_resultados(figura):
    print(f"\nÁrea: {figura.area()}")
    print(f"Perímetro: {figura.perimetro()}")

menu()