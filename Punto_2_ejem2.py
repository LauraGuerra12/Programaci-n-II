'''Diseñe un programa en Python, aplicando clases y objetos que tenga dos opciones (2 clases): convierta un número entero a número romano o convierta un número romano en un número entero. Aclaración: Recuerde que las clases tienen atributos y métodos(funciones).  '''

class NumeroEntero:
    def __init__(self, numero):
        self.numero = numero
        self.valores_romanos = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
            100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
            10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }

    def convertir_a_romano(self):
        numero = self.numero
        resultado = ""
        for valor, simbolo in self.valores_romanos.items():
            while numero >= valor:
                resultado += simbolo
                numero -= valor
        return resultado


class NumeroRomano:
    def __init__(self, romano):
        self.romano = romano
        self.valores_enteros = {
            'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
            'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
            'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
        }

    def convertir_a_entero(self):
        resultado = 0
        i = 0
        while i < len(self.romano):
            if (i + 1 < len(self.romano) and
                self.romano[i:i+2] in self.valores_enteros):
                resultado += self.valores_enteros[self.romano[i:i+2]]
                i += 2
            else:
                resultado += self.valores_enteros[self.romano[i]]
                i += 1
        return resultado


def menu():
    while True:
        print("\n--- Menú de Conversión ---\n")
        print("1. Convertir número entero a romano")
        print("2. Convertir número romano a entero")
        print("3. Salir")
        opcion = input("\nSeleccione una opción: ")
        print('')
        print('-'*30)
        print('')

        if opcion == "1":
            try:
                numero = int(input("Ingrese un número entero: "))
                if numero <= 0:
                    print("Por favor ingrese un número positivo mayor que 0.")
                    continue
                entero = NumeroEntero(numero)
                print(f"El número {numero} en romano es: {entero.convertir_a_romano()}")
            except ValueError:
                print("Entrada no válida. Debe ser un número entero.")
        
        elif opcion == "2":
            romano = input("Ingrese un número romano: ").upper()
            romano_obj = NumeroRomano(romano)
            print(f"El número romano {romano} en entero es: {romano_obj.convertir_a_entero()}")
        
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor seleccione 1, 2 o 3.")


menu()