##EJERCICIOS FUNCIONES EN PYTHON

##1. Diseñe una función llamada area_perimtero_rectangulo(base, altura) que devuelva
##el perimetro y área del rectangulo a partir de una base y una altura.
print('PUNTO 1.')
def area_perimetro_rectangulo(base, altura):
    """Calcula el área y el perímetro de un rectángulo."""
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro

def main():
    # Solicitar la base y altura del rectángulo
    base = float(input("Ingresa la base del rectángulo: "))
    altura = float(input("Ingresa la altura del rectángulo: "))
    
    # Llamar a la función y almacenar los resultados
    area, perimetro = area_perimetro_rectangulo(base, altura)
    
    # Mostrar los resultados
    print(f"El área del rectángulo es: {area:.2f}")
    print(f"El perímetro del rectángulo es: {perimetro:.2f}")

if __name__ == "__main__":
    main()
print('   ')
print('/ / ' * 16)
print('   ')


##2. Diseñe una función llamada area_perimetro_circulo(radio) que devuelva el perimetro
##y área de un círculo a partir de un radio.
print('PUNTO 2.')
import math

def area_perimetro_circulo(radio):
    """Calcula el área y el perímetro de un círculo."""
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    return area, perimetro

def main():
    # Solicitar el radio del círculo
    radio = float(input("Ingresa el radio del círculo: "))
    
    # Llamar a la función y almacenar los resultados
    area, perimetro = area_perimetro_circulo(radio)
    
    # Mostrar los resultados
    print(f"El área del círculo es: {area:.2f}")
    print(f"El perímetro del círculo es: {perimetro:.2f}")

if __name__ == "__main__":
    main()
print('   ')
print('/ / ' * 16)
print('   ')



##3. Diseñe una función hallar_mayor_menor(a,b)que tome como argumento dos
##números y devuelva el mayor y menor de ellos.
print('PUNTO 3.')
def hallar_mayor_menor(a, b):
    """Devuelve el mayor y el menor de dos números."""
    if a > b:
        mayor = a
        menor = b
    else:
        mayor = b
        menor = a
    return mayor, menor

def main():
    # Solicitar dos números al usuario
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    
    # Llamar a la función y almacenar los resultados
    mayor, menor = hallar_mayor_menor(num1, num2)
    
    # Mostrar los resultados
    print(f"El mayor número es: {mayor}")
    print(f"El menor número es: {menor}")

if __name__ == "__main__":
    main()
print('   ')
print('/ / ' * 16)
print('   ')



##4. Definir una función inversa() que calcule la inversión de una cadena.
###Por ejemplo print palabra_inversa('universidad industrial de santander')
##su programa entrega 'rednatnas ed lairtsudni dadisrevinu'
print('PUNTO 4.')
def palabra_inversa(cadena):
    """Devuelve la inversión de una cadena."""
    return cadena[::-1]

def main():
    # Solicitar una cadena al usuario
    texto = input("Ingresa una cadena de texto: ")
    
    # Llamar a la función y mostrar la cadena invertida
    print(f"La cadena invertida es: {palabra_inversa(texto)}")

if __name__ == "__main__":      #if __name__ == "__main__":: Esto garantiza que el código en el bloque main() se ejecute solo cuando el script se ejecute directamente, y no cuando se importe como un módulo en otro script.
    main()
print('   ')
print('/ / ' * 16)
print('   ')


##5. Diseñe un programa que tenga varias funciones, entre estas un menú para
##seleccionar que operación se debe realizar. Elabore funciones que nos
##permita calcular: la suma, resta, multiplicación, división, potencia, porcentaje y raices.
##Según la operación su programa debe permitir un número N de operaciones.
print('PUNTO 5.')
import math

# Funciones matemáticas
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def potencia(base, exponente):
    return base ** exponente

def porcentaje(total, porcentaje):
    return (total * porcentaje) / 100

def raiz(numero, indice=2):
    if numero >= 0:
        return numero ** (1/indice)
    else:
        return "Error: No se puede calcular la raíz de un número negativo"

# Función del menú principal
def mostrar_menu():
    print('''Menú de Operaciones: 
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Potencia
    6. Porcentaje
    7. Raíz
    8. Salir\n''')


def realizar_operacion(opcion):
    if opcion == 1:
        n = int(input("¿Cuántos números deseas sumar? "))
        resultado = 0
        for i in range(n):
            numero = float(input(f"Ingrese el número {i+1}: "))
            resultado = sumar(resultado, numero)
        print(f"Resultado de la suma: {resultado}")

    elif opcion == 2:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(f"Resultado de la resta: {restar(a, b)}")

    elif opcion == 3:
        n = int(input("¿Cuántos números deseas multiplicar? "))
        resultado = 1
        for i in range(n):
            numero = float(input(f"Ingrese el número {i+1}: "))
            resultado = multiplicar(resultado, numero)
        print(f"Resultado de la multiplicación: {resultado}")

    elif opcion == 4:
        a = float(input("Ingrese el dividendo: "))
        b = float(input("Ingrese el divisor: "))
        print(f"Resultado de la división: {dividir(a, b)}")

    elif opcion == 5:
        base = float(input("Ingrese la base: "))
        exponente = float(input("Ingrese el exponente: "))
        print(f"Resultado de la potencia: {potencia(base, exponente)}")

    elif opcion == 6:
        total = float(input("Ingrese el valor total: "))
        porc = float(input("Ingrese el porcentaje: "))
        print(f"Resultado del porcentaje: {porcentaje(total, porc)}")

    elif opcion == 7:
        numero = float(input("Ingrese el número: "))
        indice = int(input("Ingrese el índice de la raíz (2 para cuadrada, 3 para cúbica, etc.): "))
        print(f"Resultado de la raíz: {raiz(numero, indice)}")

def main():
    while True:
        mostrar_menu()
        opcion = int(input("\nSeleccione una operación (1-8): "))

        if opcion == 8:
            print("¡Hasta luego!")
            break
        elif opcion >= 1 and opcion <= 7:
            realizar_operacion(opcion)
        else:
            print("Opción no válida, por favor seleccione nuevamente.")

if __name__ == "__main__":
    main()
print('   ')
print('/ / ' * 16)
print('   ')



##6. Diseñe un programa que permita establecer la relación entre dos números ingresados y se cumplan las
##siguientes relaciones relación(a,b). Si el primer número es mayor que el segundo, debe devolver "True".
##Si el primer número es menor que el segundo, debe devolver "False" y Si ambos números son iguales, debe devolver un "Empate".
print('PUNTO 6.')
def relacion(a, b):
    """Devuelve 'True' si el primer número es mayor, 'False' si es menor, y 'Empate' si son iguales."""
    if a > b:
        return True
    elif a < b:
        return False
    else:
        return "Empate"

def main():
    # Solicitar al usuario que ingrese dos números
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    # Llamar a la función relacion y mostrar el resultado
    resultado = relacion(num1, num2)
    print(f"La relación entre los números es: {resultado}")

if __name__ == "__main__":
    main()

print('   ')
print('/ / ' * 16)
print('   ')



##7. Diseñe un algoritmo que realice el proceso de ordenar una lista dada con números enteros y estos se repartan
##en dos listas pares e impares respectivamente. Cree una función Separar(lista). Utilice los comandos
##nombrelista.sort() para ordenar la lista y nombrelista.append()
print('PUNTO 7.')
def Separar(lista):
    """Separa una lista de números en pares e impares, y las ordena."""
    lista_pares = []
    lista_impares = []
    
    lista.sort()    #Ordenar la lista original
    
    for numero in lista:      #Separar los números en pares e impares
        if numero % 2 == 0:
            lista_pares.append(numero)
        else:
            lista_impares.append(numero)
    
    return lista_pares, lista_impares

def main():
    lista_numeros = [12, 45, 2, 8, 33, 10, 7, 3, 21]    #Ejemplo de lista dada
    
    pares, impares = Separar(lista_numeros)      #Llamar a la función Separar para obtener pares e impares
    

if __name__ == "__main__":
dd    main()

print('   ')
print('/ / ' * 16)
print('   ')
