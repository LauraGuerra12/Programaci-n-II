##EJERCICIOS DE APLICACIONES

##1. Aplicando tuplas, diseñe una base de datos que permita visualizar nombres,
##apellidos, documento de identidad, dirección de residencia y número de teléfono.
print('PUNTO 1.')
base_datos = [
    ("Juan", "Guerra", "12345678", "Calle 123 #45-67", "3001234567"),
    ("Milena", "Cepeda", "87654321", "Carrera 56 #78-90", "3119876543"),
    ("Carlos", "Barrera", "11223344", "Avenida 10 #20-30", "3224567890"),
    ("Ana", "Guerra", "55667788", "Calle 22 #33-44", "3009988776"),
]

def mostrar_base_datos():
    print("Base de Datos:\n")
    print(f"{'Nombre':<10} {'Apellido':<10} {'Documento':<15} {'Dirección':<25} {'Teléfono':<12}")
    print("="*72)
    
    for registro in base_datos:
        nombre, apellido, documento, direccion, telefono = registro
        print(f"{nombre:<10} {apellido:<10} {documento:<15} {direccion:<25} {telefono:<12}")

mostrar_base_datos()
print(' ')
print(' - ' * 40)
print(' ')


##2.Crea una tupla con los meses del año, su programa debe solicitar por pantalla números al
##usuario, si el número esta entre 1 y la longitud máxima de la tupla (12), muestra el contenido
##de esa posición sino muestra un mensaje de error. El programa termina cuando el usuario introduce un cero.
print('PUNTO 2.')
meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

def mostrar_mes():
    while True:
        numero = int(input("Introduce un número entre 1 y 12 (o 0 para salir): "))

        if numero == 0:
            print("Saliendo del programa...")
            break
        elif 1 <= numero <= len(meses):
            print(f"El mes correspondiente es: {meses[numero - 1]}")
        else:
            print("Error: El número debe estar entre 1 y 12.")

mostrar_mes()
print(' ')
print(' - ' * 40)
print(' ')


##3.Modifique el programa anterior, ahora por medio de listas edite por pantalla los datos de
##las personas, cambie dirección y teléfono.
print('PUNTO 3.')
base_datos = [
    ["Juan", "Guerra", "12345678", "Calle 123 #45-67", "3001234567"],
    ["Milena", "Cepeda", "87654321", "Carrera 56 #78-90", "3119876543"],
    ["Carlos", "Barrera", "11223344", "Avenida 10 #20-30", "3224567890"],
    ["Ana", "Guerra", "55667788", "Calle 22 #33-44", "3009988776"],
]

def mostrar_base_datos():
    print("\nBase de Datos:")
    print(f"{'ID':<5} {'Nombre':<10} {'Apellido':<10} {'Documento':<15} {'Dirección':<25} {'Teléfono':<12}")
    print("="*80)
    
    for idx, registro in enumerate(base_datos):
        nombre, apellido, documento, direccion, telefono = registro
        print(f"{idx+1:<5} {nombre:<10} {apellido:<10} {documento:<15} {direccion:<25} {telefono:<12}")

def editar_datos():
    mostrar_base_datos()
    try:
        id_persona = int(input("\nIngrese el ID de la persona cuyos datos desea editar (o 0 para salir): "))
        
        if id_persona == 0:
            print("Saliendo de la edición...")
            return
        
        if 1 <= id_persona <= len(base_datos):
            nueva_direccion = input("Ingrese la nueva dirección: ")
            nuevo_telefono = input("Ingrese el nuevo número de teléfono: ")

            base_datos[id_persona - 1][3] = nueva_direccion
            base_datos[id_persona - 1][4] = nuevo_telefono

            print("\nDatos actualizados con éxito.")
        else:
            print("Error: ID inválido.")
    
    except ValueError:
        print("Error: Ingrese un número válido.")

while True:
    print("\nMenú:")
    print("1. Mostrar base de datos")
    print("2. Editar dirección y teléfono")
    print("0. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        mostrar_base_datos()
    elif opcion == "2":
        editar_datos()
    elif opcion == "0":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intente de nuevo.")
print(' ')
print(' - ' * 40)
print(' ')


##4. Escriba un programa que permita llenar una lista vacía por pantalla. Al llenarla ella
##debe ordenar los números contenidos y crear dos listas una para los números pares y otra
##para los impares. 
print('PUNTO 4.')
def llenar_lista():
    lista = []
    while True:
        try:
            numero = int(input("Introduce un número entero (o 0 para finalizar): "))
            if numero == 0:
                break
            lista.append(numero)
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")
    return lista

def separar_pares_impares(lista):
    pares = [num for num in lista if num % 2 == 0]
    impares = [num for num in lista if num % 2 != 0]
    return pares, impares

def main():
    print("Llenado de la lista:")
    lista = llenar_lista()
    
    lista.sort()

    pares, impares = separar_pares_impares(lista)

    print(f"\nLista completa ordenada: {lista}")
    print(f"Lista de números pares: {pares}")
    print(f"Lista de números impares: {impares}")

if __name__ == "__main__":
    main()
print(' ')
print(' - ' * 40)
print(' ')



##5. Escribir una función sumar() y una función multiplicar(), estas deben sumar y multiplicar
##respectivamente todos los números de una lista. #Por ejemplo: sumar([1,2,3,4]) debería devolver
##10 y multiplicar([1,2,3,4]) debería devolver 24.
print('PUNTO 5.')
def sumar(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma

def multiplicar(lista):
    producto = 1
    for num in lista:
        producto *= num
    return producto

lista_ejemplo = [1, 2, 3, 4]

resultado_suma = sumar(lista_ejemplo)
resultado_multiplicacion = multiplicar(lista_ejemplo)

print(f"Suma de {lista_ejemplo}: {resultado_suma}")
print(f"Multiplicación de {lista_ejemplo}: {resultado_multiplicacion}")
print(' ')
print(' - ' * 40)
print(' ')



##6. Diseñe un algoritmo que le permita crear una lista con nombres de estudiantes (N nombres),
##su programa debe permitir buscar si los nombres están contenidos en la lista, la consulta
##solicita nombres y verifica si están o no.
print('PUNTO 6.')
def llenar_lista():
    lista_estudiantes = []
    while True:
        nombre = input("Introduce el nombre del estudiante (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break
        lista_estudiantes.append(nombre)
    return lista_estudiantes

def buscar_nombre(lista_estudiantes):
    nombre_buscar = input("\nIntroduce el nombre que deseas buscar: ")
    if nombre_buscar in lista_estudiantes:
        print(f"{nombre_buscar} está en la lista.")
    else:
        print(f"{nombre_buscar} NO está en la lista.")

def main():
    print("Llenado de la lista de estudiantes:")
    lista_estudiantes = llenar_lista()
    
    print("\nLista de estudiantes creada con éxito.")
    
    while True:
        print("\nMenú:")
        print("1. Buscar un nombre")
        print("0. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            buscar_nombre(lista_estudiantes)
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
print(' ')
print(' - ' * 40)
print(' ')
      

