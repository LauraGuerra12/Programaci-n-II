

#1. 
# name = input('Por favor ingrese su nombre: ')
# last_name = input('Por favor ingrese su apellido: ')
# age = input('Por favor ingrese su edad: ')
# address = input('Por favor ingrese su direccion: ')
# number_phone = input('Por favor ingrese su teléfono: ')
# gender = input('Por favor ingrese su genero: ')
# print(f'{'Su nombre es '}{name}{', su apellido es '}{last_name}{',su edad es '}{age}{', su dirección es '}{address}{', su numero de telefono es '}{number_phone}{'y su genero es'}{gender}')


#2

#3.
# import math
# a = float(input('Por favor ingrese un número: '))
# b = float(input('Por favor ingrese otro número: '))
# c = float(input('Por favor ingrese otro número: '))
# print(f'{'La media arimetica de los numeros '}{a}{' '}{b}{' y '}{c}{' es: '}{(a+b+c)/3}')

#4
# weight = float(input('Por favor digite su peso en kg: '))
# height = float(input('Por favor digite su altura en metros: ')) 
# imc = weight/(height**2)
# print('El IMC suyo es de :', round(imc,3))

#5
# temp = float(input('Escriba la temperatura en grados Fahrenheir: '))
# print('La temperatura en grados Celsius es: ', round((temp-32)/1.8,3),'°C')

#6
# temp = float(input('Escriba la temperatura en grados Fahrenheir: '))
# c = round((temp-32)/1.8,3)
# print('La temperatura en Kelvin es: ',c+273.15,'K')

#7
# temp = float(input('Escriba la temperatura en Kelvin: '))
# print('La temperatura en grados Celsius es: ', round(temp-273.15,3),'K')

#8 NOTA // dice el resultado de la división y % lo que sobra de la división
# total_seconds = float(input('Escriba los segundos a convertir: '))
# hours = total_seconds // 3600
# remaining_secods = total_seconds % 3600 
# minutes = remaining_secods // 60
# remaining_secods1 = remaining_secods % 60
# seconds = remaining_secods1
# print(f'Las horas son {hours}, los minutos son {minutes} y los segundos {seconds}')

#9
# import math
# cateto_a = float(input("Ingrese la longitud del primer cateto (a): "))
# cateto_b = float(input("Ingrese la longitud del segundo cateto (b): "))
# hipotenusa = round(math.sqrt(cateto_a*2 + cateto_b*2))
# area = (cateto_a * cateto_b) / 2
# perimetro = cateto_a + cateto_b + hipotenusa
# print(f'El cateto a es {cateto_a}, el cateto b es {cateto_b}, la hipotenusa es {hipotenusa}, el área es {area} y el perimetro es {perimetro}')

#10
#import math
#radio = float(input("Ingrese el radio del círculo: "))
#area = round(math.pi * radio**2,3)
#perimetro = round(2 * math.pi * radio,3)
#circunferencia = round(2 * math.pi * radio)
# print(f'La circunferencia es{circunferencia}, el area es {area}, el área es {area}, el radio es {radio}y el perimetro es {perimetro}') 
