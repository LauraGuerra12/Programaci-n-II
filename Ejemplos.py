#EJEMPLO 1
##print("Hola Mundo")

#EJEMPLO 2
##libro = "El programador"

#EJEMPLO 3
##numeros = [23, 45, 16, 3, 999]
##print(numeros[0])

#EJEMPLO 4
##jugadores = {
##    10: 'James Rodriguez',
##    7: 'Cristiano Ronaldo'
##}
##print(jugadores[10])

#EJEMPLO 5
##pi = 3.141592

#EJEMPLO 6
##print(1 + 1)  #sumar
##print(1 - 1)  #restar
##print(10*2)   #multiplicar
##print(10/2)   #dividir

#EJEMPLO 7
##print(4 == 4)
##print(4 == '4')
##print(4 != 5)
##print(4 < 5)
##print(4 >= 5)

#EJEMPLO 8
##entero = 100
##print(entero is entero)

#EJEMPLO 9
##print(True and True)
##print(True and False)
##print(False and True)
##print(False and False)

#EJEMPLO 10
##print(True or True)
##print(True or False)
##print(False or True)
##print(False or False)

#EJEMPLO 11
##autorizado = True
##
##if autorizado:
##    print('Puede ingresar')
##else:
##    print('No puede ingresar')

#EJEMPLO 12
##entero = 100
##
##if entero == 99:
##    print('Es 99')
##elif entero == 100:
##    print('Es 100')
##else:
##    print('No es 99, ni 100')

#FUNCIONES def
#EJEMPLO 13
##def sumar(primero, segundo):
##    return primero + segundo
##
##resultado = sumar(3, 4)
##print('El resultado es: ', resultado)

#EJEMPLO 14   (Ordena los numeros)
##def quicksort(lista):
##    if len(lista) <= 1:
##        return lista
##
##    pivote = lista[0]
##    izquierda = []
##    derecha = []
##    for i in range(1, len(lista)):
##        izquierda.append(lista[i]) if lista[i] < pivote else derecha
##        
##    return quicksort(izquierda) + [pivote] + quicksort(derecha)
##
##numeros = [23, 45, 16, 37, 3, 99, 22]
##listaOrdenada = quicksort(numeros)
##print(listaOrdenada)
