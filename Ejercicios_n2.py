
#Ejercicios IF-ELIF-ELSE-FOR-WHILE

##1 Empleando el condicional IF realice el diseño de un algoritmo que solicite por pantalla los datos de unos empleados:
##Nombre y Apellido, documento de identidad, sueldo. Con estos datos su programa debe saber que personas ganan superior 
##al salario mínimo y mostrar al finalizar la ejecución los datos del empleado e indicar si gana o no superior al salario mínimo en Colombia.
print("PUNTO 1.")
n_trabajadores = input('Ingrese la cantidad de empleados: ')
list_trabajadores = []
salario_minimo = 1160000  #Salario mínimo actualizado

#Recolectar datos de los trabajadores
for i in range(int(n_trabajadores)):
    nombre = input(f'Ingrese el Nombre de la persona {i + 1}: ')
    apellido = input(f'Ingrese el Apellido de la persona {i + 1}: ')
    documento = input(f'Ingrese el n° Documento de la persona {i + 1}: ')
    salario = int(input(f'Ingrese el Salario de la persona {i + 1}: '))
    persona = [nombre, apellido, documento, salario]  # Crear una lista con los datos
    list_trabajadores.append(persona)

#Mostrar información de cada trabajador
for i in range(int(n_trabajadores)):
    nombre_completo = f"{list_trabajadores[i][0]} {list_trabajadores[i][1]}"
    documento = list_trabajadores[i][2]
    salario = list_trabajadores[i][3]

    if salario >= salario_minimo:
        estado = "Gana el salario mínimo o gana más del salario mínimo."
    else:
        estado = "No gana el salario mínimo."

    print(f'Empleado: {nombre_completo}')
    print(f'N° Documento: {documento}')
    print(f'Salario: {salario} y {estado}')
    print('*' * 40)  #Separador entre empleados
print('   ')
print('-' * 50)
print('   ')

##2. Construir un programa que calcule y muestre por pantalla las  raíces de la ecuación de segundo grado de coeficientes reales. El programa debe 
##diferenciar los diferentes casos que puedan surgir: la existencia de dos raíces reales distintas, de dos raíces reales iguales y de dos raíces complejas. 
##Nota: se recomienda el empleo de sentencias if_else [Ecuacion cuadratica]
print("PUNTO 2.")
import math

a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

discriminante = b**2 - 4*a*c   #Calcular el discriminante

if discriminante > 0:          #Condiciones para los diferentes casos
    #Dos raíces reales distintas
    raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
    raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
    print(f'La ecuación tiene dos raíces reales distintas: x1 = {raiz1} y x2 = {raiz2}')
elif discriminante == 0:
    raiz = -b / (2*a)    #Dos raíces reales iguales
    print(f'La ecuación tiene dos raíces reales iguales: x1 = x2 = {raiz}')
else:
    real = -b / (2*a)    #Dos raíces complejas
    imaginario = math.sqrt(-discriminante) / (2*a)
    print(f'La ecuación tiene dos raíces complejas: x1 = {real} + {imaginario}i y x2 = {real} - {imaginario}i')
print('   ')
print('-' * 50)
print('   ')



##3. Escribir un programa que solicite al usuario una letra. Al ingresarla por teclado si es una vocal, muestre el mensaje “es vocal”. 
##Se debe validar que el usuario ingrese sólo un carácter. Al ingresar un string de más de un carácter, informarle que no se puede procesar el dato.
print("PUNTO 3.")
num = [str(i) for i in range(10)]      #Lista de números como cadenas
vocales = ['a', 'e', 'i', 'o', 'u']     #Lista de vocales

while True:
    vocal = input('Ingrese una vocal: ')
    if len(vocal) != 1:
        print('Error: Debe ingresar solo una (1) vocal.')
        continue        #Volver a solicitar un nuevo dato
    if vocal in num:
        print('Usted digitó un número.')
        break
    elif vocal.lower() in vocales:
        print('Usted digitó una vocal.')
        break
    else:
        print('Usted no digitó una vocal.')
        break
print('   ')
print('-' * 50)
print('   ')



##4. Diseñe un programa empleando las condiciones if-elif-else. Dicho algoritmo debe ser para hacer un menú de acceso a una calculadora. 
##Incluya todas las operaciones aritméticas, comparar números pares e impares , sacar porcentajes, hallar valores de razones trigonométricas.
print("PUNTO 4.")
import math as m

# Mostrar el menú
print('''CALCULADORA
MARQUE:
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Comparar si un número es par o impar
    6. Calcular un porcentaje
    7. Calcular razones trigonométricas''')

while True:
    v0 = input('Ingrese la opción con la que desea trabajar: ')
    
    if v0 == '1':     #Suma
        num1 = float(input('Ingrese el primer número: '))
        num2 = float(input('Ingrese el segundo número: '))
        print(f'La operación {num1} + {num2} = {num1 + num2}')
        break
        
    elif v0 == '2':    #Resta
        num1 = float(input('Ingrese el primer número: '))
        num2 = float(input('Ingrese el segundo número: '))
        print(f'La operación {num1} - {num2} = {num1 - num2}')
        break
        
    elif v0 == '3':    #Multiplicación
        num1 = float(input('Ingrese el primer número: '))
        num2 = float(input('Ingrese el segundo número: '))
        print(f'La operación {num1} * {num2} = {num1 * num2}')
        break
        
    elif v0 == '4':    #División
        num1 = float(input('Ingrese el primer número: '))
        num2 = float(input('Ingrese el segundo número: '))
        if num2 == 0:
            print('Error: División entre cero no permitida.')
        else:
            print(f'La operación {num1} / {num2} = {num1 / num2}')
        break
        
    elif v0 == '5':    #Comparar si un número es par o impar
        num1 = int(input('Ingrese un número: '))
        if num1 % 2 == 0:
            print(f'El número {num1} es un número par.')
        else:
            print(f'El número {num1} es un número impar.')
        break
        
    elif v0 == '6':    #Calcular un porcentaje
        num1 = float(input('Ingrese el número: '))
        num2 = float(input('Ingrese el porcentaje que desea calcular: '))
        print(f'El {num2}% de {num1} es {(num2 / 100) * num1}')
        break
        
    elif v0 == '7':    #Calcular razones trigonométricas
        p = m.pi
        print('Considere el número en radianes. PARA ESCRIBIR EL NÚMERO PI (3.1416...), escriba "pi".')
        num1 = input('Ingrese un número: ')
        
        # Convertir 'pi' a valor numérico
        if num1 == 'pi':
            t = p
        else:
            t = float(num1)
        
        razon = input('''Ingrese la opción de la razón trigonométrica que desea: 
        1. sin(x)
        2. cos(x)
        3. tan(x)\n''')
        
        if razon == '1':
            print(f'El sin({num1}) es {round(m.sin(t), 3)}')
        elif razon == '2':
            print(f'El cos({num1}) es {round(m.cos(t), 3)}')
        elif razon == '3':
            print(f'La tan({num1}) es {round(m.tan(t), 3)}')
        else:
            print('Opción inválida.')
        break
        
    else:
        print('Por favor, digite una opción correcta.')
print('   ')
print('-' * 50)
print('   ')



##5. Escriba un programa que me permita cambiar unidades de longitud. Su programa debe solicitar escoger en que unidad va ingresar la medida y en que unidad 
##la quiere visualizar en pantalla, su programa debe disponer de conversiones (metro, kilómetros, centímetros, millas, yardas, pies o pulgadas). 
##Ejemplo: pida una distancia en pulgadas o pies y que escriba esa distancia en centímetros. Se recuerda que una pulgada son 2,54 cm y un pie son doce pulgadas.
print('PUNTO 5.')
#Mostrar el menú para seleccionar la unidad de ENTRADA
print('''INGRESE EL TIPO DE DATO DE SU MEDIDA INICIAL:
 1. Metro
 2. Kilómetros
 3. Centímetros
 4. Millas
 5. Yardas
 6. Pies
 7. Pulgadas\n''')

opciones = ['1', '2', '3', '4', '5', '6', '7']  #Lista de opciones válidas


while True:       #Solicitar tipo de dato inicial
    v0 = input('Ingrese el tipo de dato: ')
    if v0 in opciones:
        break
    else:
        print('¡INGRESE UNA OPCIÓN VÁLIDA!')

while True:      #Solicitar el valor de la medida
    try:
        d0 = float(input('Ingrese el valor de la medida: '))
        break     #Si la conversión a float es exitosa, salir del bucle
    except ValueError:
        print('¡INGRESE UN VALOR NUMÉRICO VÁLIDO!')

# Convertir la medida inicial a metros
if v0 == '1':
    f0 = d0             #Metros
elif v0 == '2':
    f0 = d0 * 1000      #Kilómetros a metros
elif v0 == '3':
    f0 = d0 / 100       #Centímetros a metros
elif v0 == '4':
    f0 = d0 * 1609.34   #Millas a metros
elif v0 == '5':
    f0 = d0 * 0.9144    #Yardas a metros
elif v0 == '6':
    f0 = d0 * 0.3048    #Pies a metros
elif v0 == '7':
    f0 = d0 * 0.0254    #Pulgadas a metros

#Mostrar el menú para seleccionar la unidad de SALIDA
print('''INGRESE LA MEDIDA A LA QUE DESEA CONVERTIR:
 1. Metro
 2. Kilómetros
 3. Centímetros
 4. Millas
 5. Yardas
 6. Pies
 7. Pulgadas\n''')


while True:    #Solicitar la unidad de salida
    v1 = input('Ingrese el tipo que quiere como respuesta: ')
    if v1 in opciones:
        break
    else:
        print('¡INGRESE UNA OPCIÓN VÁLIDA!')

#Convertir la medida en metros a la unidad solicitada
if v1 == '1':
    f1 = f0            #Metros
elif v1 == '2':
    f1 = f0 / 1000     #Metros a kilómetros
elif v1 == '3':
    f1 = f0 * 100      #Metros a centímetros
elif v1 == '4':
    f1 = f0 / 1609.34  #Metros a millas
elif v1 == '5':
    f1 = f0 * 1.09361  #Metros a yardas
elif v1 == '6':
    f1 = f0 * 3.28084  #Metros a pies
elif v1 == '7':
    f1 = f0 * 39.3701  #Metros a pulgadas

print(f'La conversión da: {f1}')    #Mostrar el resultado de la conversión
print('   ')
print('-' * 50)
print('   ')



##6. Escriba un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A, candidato B, candidato C y voto 
##en blanco. Según el candidato elegido (A, B, C ó Voto blanco) se le debe imprimir el mensaje “Usted ha votado por el candidato #”. 
##Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.
print('PUNTO 6.')
print('''INGRESE EL CANDIDATO POR EL QUE DESEA VOTAR:
 1. Candidato A
 2. Candidato B
 3. Candidato C
 4. Voto en blanco\n''')

opciones = {
    '1': 'Candidato A',
    '2': 'Candidato B',
    '3': 'Candidato C',
    '4': 'Voto en blanco'
}

while True:
    voto = input('Ingrese la opción para votar: ')
    if voto in opciones:
        print(f'Usted ha votado por {opciones[voto]}')  # Mostrar la opción elegida
        break
    else:
        print('¡OPCIÓN ERRÓNEA! Por favor, ingrese una opción válida.')
print('   ')
print('-' * 50)
print('   ')


##7. Diseñe un algoritmo que le permita crear una lista con nombres de estudiantes (N nombres), su programa debe permitir buscar si los nombres están 
##contenidos en la lista, la consulta solicita nombres y verifica si están o no. Recomiendo uso for e if
print('PUNTO 7.')
while True:
    try:
        n = int(input('Ingrese la cantidad de nombres que desea: '))
        break       #Si la conversión a int es exitosa, salimos del bucle
    except ValueError:
        print('¡INGRESE UN NÚMERO VÁLIDO!')

lista = []      #Crear la lista de nombres
for i in range(n):
    name = input(f'Ingrese el {i + 1}° nombre: ')
    lista.append(name)

print("Lista de nombres ingresados:", lista)      #Mostrar la lista de nombres ingresados

search = input('Ingrese el nombre que desea consultar: ')   #Solicitar el nombre a buscar

#Verificar si el nombre está en la lista
if search in lista:
    posicion = lista.index(search)       #Obtener la posición      #Encontrar la posición del nombre
    print(f'El nombre "{search}" se encuentra en la posición {posicion + 1} de la lista.')
else:
    print(f'El nombre "{search}" no se encuentra en la lista de estudiantes ingresada.')
print('   ')
print('-' * 50)
print('   ')




##8. Escribir un programa que permita al usuario ingresar por teclado 5 números enteros, que pueden ser positivos o negativos. Al finalizar, 
##mostrar la sumatoria de los números negativos y el promedio de los positivos. Recuerde que no es posible dividir por cero, por lo que es necesario 
##evitar que el programa arroje un error si no se ingresaron números positivos.
print('PUNTO 8.')
lista_p = []
lista_n = []

for i in range(5):    #Solicitar al usuario que ingrese 5 números enteros
    while True:
        try:
            num = int(input(f'Ingrese el {i + 1}° número: '))
            #Clasificar el número como positivo o negativo
            if num < 0:
                lista_n.append(num)  # Agregar a la lista de negativos
                break
            else:
                lista_p.append(num)  # Agregar a la lista de positivos
                break                
        except ValueError:
            print('¡SOLO NÚMEROS ENTEROS!')

suma_negativos = sum(lista_n)     #Calcular la suma de los números negativos

# Calcular el promedio de los números positivos si hay algún número positivo
if lista_p:  # Verificar si la lista de positivos no está vacía
    promedio_positivos = round(sum(lista_p) / len(lista_p), 3)
else:
    promedio_positivos = 0  # Si no hay positivos, establecer el promedio en 0

print(f'La suma de los números negativos es: {suma_negativos}')
print(f'El promedio de los números positivos es: {promedio_positivos}')
print('   ')
print('-' * 50)
print('   ')




##9. Escriba un programa que pida números enteros mientras sean cada vez más grandes, al digitar un número menor que el anterior debe imprimir 
##un mensaje diciendo que ese número es menor y terminar el programa usando while.
print('PUNTO 9.')
numeros = []        #Inicializar la lista para almacenar los números ingresados

while True:         #Solicitar el primer número al usuari
    try:
        entrada = int(input('Ingrese un número entero: '))
        numeros.append(entrada)  #Agregar el primer número a la lista
        break
    except ValueError:
        print('¡DIGITE UN NÚMERO ENTERO!')

while True:        #Continuar solicitando números mientras sean mayores que el anterior
    try:
        entrada = int(input('Ingrese un número entero: '))
        if entrada > numeros[-1]:  # Comparar con el último número ingresado
            numeros.append(entrada)  # Agregar el nuevo número a la lista
        else:
            print(f'¡El número {entrada} es menor o igual que el anterior ({numeros[-1]}). Terminando el programa!')
            break
    except ValueError:
        print('¡DIGITE UN NÚMERO ENTERO!')

print('   ')
print('-' * 50)
print('   ')



##10. Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir cuántas letras mayúsculas tiene.
print('PUNTO 10.')
a = 'si'
while a.lower() == 'si':
    s = input('Ingrese una cadena: ')
    Mayus = 0
    for i in s:
        if i.isupper() == True:
            Mayus = Mayus + 1
    print(f'La cadena {s} tiene {Mayus} mayusculas')
    a = input('¿Desea ingresar otra cadena?, (si/no): ')
    a = a.lower()
print('   ')
print('-' * 50)
print('   ')



##11. Diseñe un algoritmo que permita jugar piedra, papel y tijera. Su programa debe tener dos modos: jugar contra el pc o multijugador(dos jugadores). 
##Tenga en cuenta que pueden existir empates. Su programa debe solicitar el ID del jugador y permitir varias rondas hasta que no se desee jugar más, 
##así mismo debe llevar un contador de puntos para al finalizar la partida decir quien es el ganador.
print('PUNTO 11.')
import random

def juego_piedra_papel_tijera():
    print("Bienvenido al juego de Piedra, Papel o Tijera!")
    
    #Solicitar modo de juego
    while True:
        modo = input("Seleccione el modo de juego:\n1. Jugar contra el PC\n2. Multijugador\nIngrese 1 o 2: ")
        if modo in ['1', '2']:
            break
        else:
            print("¡Opción no válida! Por favor, elija 1 o 2.")
    
    #Inicializar los puntos
    puntos_jugador1 = 0
    puntos_jugador2 = 0

    #Diccionario para la elección
    elecciones = {1: "Piedra", 2: "Papel", 3: "Tijera"}

    while True:
        #Jugar una ronda
        if modo == '1':
            #Jugar contra el PC
            jugador1 = input("Ingrese su ID (Jugador 1): ")
            jugador2 = "PC"
            
            while True:
                try:
                    eleccion_jugador1 = int(input(f"{jugador1}, elige:\n1. Piedra\n2. Papel\n3. Tijera\nIngrese su opción: "))
                    if eleccion_jugador1 in [1, 2, 3]:
                        break
                    else:
                        print("¡Opción no válida! Elija 1, 2 o 3.")
                except ValueError:
                    print("¡Por favor, ingrese un número válido!")

            eleccion_jugador2 = random.randint(1, 3)       #PC elige al azar

        else:
            #Jugar entre dos jugadores
            jugador1 = input("Ingrese el ID del Jugador 1: ")
            jugador2 = input("Ingrese el ID del Jugador 2: ")
            
            while True:
                try:
                    eleccion_jugador1 = int(input(f"{jugador1}, elige:\n1. Piedra\n2. Papel\n3. Tijera\nIngrese su opción: "))
                    if eleccion_jugador1 in [1, 2, 3]:
                        break
                    else:
                        print("¡Opción no válida! Elija 1, 2 o 3.")
                except ValueError:
                    print("¡Por favor, ingrese un número válido!")
            
            while True:
                try:
                    eleccion_jugador2 = int(input(f"{jugador2}, elige:\n1. Piedra\n2. Papel\n3. Tijera\nIngrese su opción: "))
                    if eleccion_jugador2 in [1, 2, 3]:
                        break
                    else:
                        print("¡Opción no válida! Elija 1, 2 o 3.")
                except ValueError:
                    print("¡Por favor, ingrese un número válido!")

        #Mostrar las elecciones
        print(f"\n{jugador1} eligió: {elecciones[eleccion_jugador1]}")
        if modo == '1':
            print(f"{jugador2} (PC) eligió: {elecciones[eleccion_jugador2]}")
        else:
            print(f"{jugador2} eligió: {elecciones[eleccion_jugador2]}")

        #Determinar el resultado
        if eleccion_jugador1 == eleccion_jugador2:
            print("¡Es un empate!")
        elif (eleccion_jugador1 == 1 and eleccion_jugador2 == 3) or \
             (eleccion_jugador1 == 2 and eleccion_jugador2 == 1) or \
             (eleccion_jugador1 == 3 and eleccion_jugador2 == 2):
            print(f"¡{jugador1} gana esta ronda!")
            puntos_jugador1 += 1
        else:
            print(f"¡{jugador2} gana esta ronda!")
            puntos_jugador2 += 1
        
        print(f"Puntos hasta ahora: {jugador1}: {puntos_jugador1}, {jugador2}: {puntos_jugador2}\n")
        
        #Preguntar si se desea jugar otra ronda
        continuar = input("¿Desea jugar otra ronda? (si/no): ").strip().lower()
        if continuar != 'si':
            break

    #Mostrar el ganador final
    print("\nJuego terminado.")
    print(f"Puntos finales: {jugador1}: {puntos_jugador1}, {jugador2}: {puntos_jugador2}")
    if puntos_jugador1 > puntos_jugador2:
        print(f"¡{jugador1} es el ganador final!")
    elif puntos_jugador1 < puntos_jugador2:
        print(f"¡{jugador2} es el ganador final!")
    else:
        print("¡Es un empate en la partida final!")

#Ejecutar el juego
juego_piedra_papel_tijera()































