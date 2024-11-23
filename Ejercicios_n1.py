#EJERCICIOS DE PRACTICA CLASE 1, 10 DE AGOSTO 2024

#1. Diseñe un programa en Python donde por pantalla se 
# solicite: el nombre, apellido, edad, dirección, número de teléfono y genero. 
# Al finalizar el ingreso de datos deben aparecer todos en pantalla. 
print('PUNTO 1.')
nombre = input('Por favor ingrese su nombre: ')
apellido = input('Por favor ingrese su apellido: ')
edad = int(input('Por favor ingrese su edad: '))
dirección = input('Por favor ingrese su dirección: ')
n_celular = int(input('Por favor ingrese su teléfono: '))
género = input('Por favor ingrese su género: ')
print('-' * 50)
print(f'{'Nombre: '}{nombre}')
print(f'{'Apellido: '}{apellido}')
print(f'{'Edad: '}{edad}{' años'}')
print(f'{'Dirección es: '}{dirección}')
print(f'{'Número de telefono: '}{n_celular}')
print(f'{'Género: '}{género}')
print('   ')
print('/ / ' * 16)
print('   ')

#2. Diseñe un programa empleando Python donde pueda realizar las operaciones básicas 
# de matemáticas (suma, resta, multiplicación, división, raices, potencia y porcentajes). 
# Su programa debe mostrar todas las operaciones y a medida que va mostrando en pantalla los 
# resultados debe solicitar los siguientes datos sucesivamente.
print('PUNTO 2.')
print('SUMA')
a = float(input('Por favor digite el primer número: '))
b = float(input('Por favor digite el segundo número: '))
print(f'{'La suma es = '}{a+b}')
print('-' * 50)
print('RESTA')
##c = float(input('Por favor digite el primer número: '))
##d = float(input('Por favor digite el segundo número: '))
##print(f'{'La resta es= '}{c-d}')
print(f'{'La resta de (a-b) es = '}{a-b}')
print(f'{'La resta de (b-a) es = '}{b-a}')
print('-' * 50)
print('MULTIPLICACIÓN')
##e = float(input('Por favor digite el primer número: '))
##f = float(input('Por favor digite el segundo número: '))
##print(f'{'La multiplicacion es= '}{e*f}')
print(f'{'La multiplicación es = '}{a*b}')
print('-' * 50)
print('RAICES')
##g = float(input('Por favor digite el primer número: '))
##h = float(input('Por favor digite el segundo número: '))
##print(f'{'la raiz {h} de {g} es= '}{round(g**(1/h))}')
print(f'{'la raíz {a} de {b} es = '}{round(b**(1/a))}')
print(f'{'la raíz {b} de {a} es= '}{round(a**(1/b))}')
print('-' * 50)
print('POTENCIA')
##i = float(input('Por favor digite el primer número: '))
##j = float(input('Por favor digite el segundo número: '))
##print(f'{'La potencia de {i} elevado a {j} es= '}{i**j}')
print(f'{'La potencia de {a} elevado a {b} es= '}{a**b}')
print(f'{'La potencia de {b} elevado a {a} es= '}{b**a}')
print('-' * 50)
print('PORCENTAJES')
##k = float(input('Por favor digite el primer número: '))
##l = float(input('Por favor digite el segundo número: '))
##print(f'{'El {k}% de {l} es= '}{(k*l)/100}')
print(f'{'El {a}% de {b} es= '}{(a*b)/100}')
print(f'{'El {b}% de {a} es= '}{(b*a)/100}')
print('   ')
print('/ / ' * 16)
print('   ')

#3. Escriba un programa en Python donde cree tres variables y por pantalla solicite los números. 
# Al finalizar el cargue de datos se debe calcular la media aritmética e imprimirla en pantalla.
print('PUNTO 3.')
import math
a = float(input('Por favor ingrese el primer número: '))
b = float(input('Por favor ingrese el segundo número: '))
c = float(input('Por favor ingrese el tercer número: '))
print(f'{'La media arimética de los números '}{a}{' '}{b}{' y '}{c}{' es = '}{(a+b+c)/3}')
print('   ')
print('/ / ' * 16)
print('   ')

#4. Escriba un programa en Python que pida el peso (en kilogramos) y la altura (en metros) de una persona y 
# que calcule su índice de masa corporal (imc). imc se calcula con la fórmula imc = peso / altura2
print('PUNTO 4.')
peso = float(input('Por favor dígite su peso en kilogramos (kg): '))
altura = float(input('Por favor dígite su altura en metros (m): ')) 
imc = peso/(altura**2)
print('Su Índice de Masa Corporal (IMC) es de =', round(imc,3))
print('   ')
print('/ / ' * 16)
print('   ')

#5. Escriba un programa que pida una temperatura en grados Fahrenheit y que escriba esa temperatura en grados Celsius. 
# La relación entre grados Celsius (C) y grados Fahrenheit (F) es la siguiente: C = (F - 32) / 1,8
print('PUNTO 5.')
temperatura = float(input('Escriba la temperatura en grados Fahrenheit (°F): '))
print('La temperatura en grados Celsius (°C) es = ', round((temperatura-32)/1.8,3),'°C')
print('   ')
print('/ / ' * 16)
print('   ')

#6. Escriba un programa que pida una temperatura en grados Fahrenheit y 
# que escriba esa temperatura en grados Kelvin
print('PUNTO 6.')
temper = float(input('Escriba la temperatura en grados Fahrenheit (°F): '))
c = round((temper-32)/1.8, 3)
print('La temperatura en Kelvin (°K) es = ',c+273.15,'°K')
print('   ')
print('/ / ' * 16)
print('   ')

#7. Escriba un programa que pida una temperatura en grados Kelvin y 
# que escriba esa temperatura en grados Celsius
print('PUNTO 7.')
temp = float(input('Escriba la temperatura en Kelvin (°K): '))
print('La temperatura en grados Celsius (°C) es= ', round(temp-273.15,3),'°C')
print('   ')
print('/ / ' * 16)
print('   ')

#8. Escriba un programa que pida una cantidad de segundos y que escriba cuántas horas, minutos y segundos son:
#  NOTA // dice el resultado de la division y % lo que sobra de la division
print('PUNTO 8.')
segundos_totales = int(input('Ingrese la cantidad de segundos que desea convertir: '))
horas = segundos_totales // 3600
segundos_restantes = segundos_totales % 3600
minutos = segundos_restantes // 60
segundos_finales = segundos_restantes % 60
print(f'{segundos_totales} segundos son {horas} horas, {minutos} minutos y {segundos_finales} segundos.')
print('   ')
print('/ / ' * 16)
print('   ')

#9. Elabore un programa que sirva para hallar el perímetro y área de  un triangulo rectángulo. 
# Solicite todos los datos necesarios por pantalla y el usuario los debe ingresar. 
# Al finalizar el programa debe imprimir la información de los mismos.
print('PUNTO 9.')
import math
cateto_a = float(input("Ingrese la longitud del primer cateto (a): "))
cateto_b = float(input("Ingrese la longitud del segundo cateto (b): "))
hipotenusa = round(math.sqrt(cateto_a**2 + cateto_b**2))
area = (cateto_a * cateto_b) / 2
perimetro = cateto_a + cateto_b + hipotenusa
print(f'{'El cateto a es= '}{cateto_a}')
print(f'{'El cateto b es= '}{cateto_b}')
print(f'{'La hipotenusa es= '}{hipotenusa}')
print(f'{'El área es= '}{area}')
print(f'{'El perimetro es= '}{perimetro}')
print('   ')
print('/ / ' * 16)
print('   ')

#10. Elabore un programa que sirva para hallar el perimetro y área de  un circulo. 
# Solicite todos los datos necesarios por pantalla y el usuario los debe ingresar. 
# Al finalizar el programa debe imprimir la información de los mismos. 
print('PUNTO 10.')
import math
radio = float(input("Ingrese el radio del circulo: "))
area = round(math.pi * radio**2,3)
perimetro = round(2 * math.pi * radio,3)
circunferencia = round(2 * math.pi * radio)
print(f'La circunferencia es {circunferencia}')
print(f'{'El área es = '}{area}')
print(f'{'El área es = '}{area}')
print(f'{'El radio es = '}{radio}')
print(f'{'El perimetro es = '}{perimetro}')

