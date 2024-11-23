import math

#Parte 1
##cadena = input("Ingrese una cadena de texto \n ")
##print(cadena.isupper())


#Parte 2
##cont = 0
##a = "si"
##while a == "si":
##    cadena = input("Ingrese una cadena de texto \n ")
##    for letra in cadena:
##        if letra.isupper() == True:
##            cont += 1
##    print(cont)
##    a = input("Desea escribir otra cadena: si o no ")
    

# #Parte 3
# a = "si"
# while a == "si":
#    cont = 0
#    cadena = input("Ingrese una cadena de texto \n ")
#    for letra in cadena:
#        if letra.isupper() == True:
#            cont += 1
#    print(cont)
#    a = input("Desea escribir otra cadena: si o no ")

# print(cadena.isupper())


#Parte 4
##Crear Funciones

#Parte4.1
##def hoy():
##    print("Bienvenido a clase")

#Parte4.2
##def hoy():
##    print("Bienvenido a clase")
##
##a = hoy()

#Parte4.3
##def hoy():
##    print("Bienvenido a clase")
##
##a = hoy()
##print(a)

#Parte4.4
##def Sumar(num1, num2):
##    global resultado
##    resultado = num1 + num2
##    print(resultado)
##
##a = float(input("Ingrese un numero "))
##b = float(input("Ingrese un numero "))
##Sumar(a,b)

#Parte4.5
##def Sumar(num1, num2):
##    global resultado
##    resultado = num1 + num2
##    return resultado   #return debe tener donde almacenar, despues de la linea de RERUTN  no lee mas codigo. Es la ultima linea.
##
##a = float(input("Ingrese un numero "))
##b = float(input("Ingrese un numero "))
##laura = Sumar(a,b)
##print(laura)


#Parte 5
#Calcular el perimetro del triangulo

#Parte 5.1
##def perimetro_triangulo ( cateto1:float, cateto2:float)->float: 
##    hipotenusa = calcular_hip(cateto1, cateto2)
##    return cateto1+cateto2+hipotenusa
##
##def calcular_hip(cateto1:float, cateto2:float)->float:
##    suma_cuadrados = (cateto1**2)+(cateto2**2)
##    hipotenusa = pow(suma_cuadrados, 0.5)
##    return hipotenusa
##
##cadena_cat_1 = input("Indique la longitud del primer cateto: ")
##cadena_cat_2 = input("Indique la longitud del segundo cateto: ")
##cat_1 = float(cadena_cat_1)
##cat_2 = float(cadena_cat_2)
##perimetro = perimetro_triangulo(cat_1,cat_2)
##print("El perímetro de un triángulo rectángulo que tenga catetos de longitud",cat_1,"y",cat_2,"es",perimetro)

#Parte 5.2
##def perimetro_triangulo ( cateto1:float, cateto2:float):#->float: 
##    hipotenusa = calcular_hip(cateto1, cateto2)
##    return cateto1+cateto2+hipotenusa
##
##def calcular_hip(cateto1:float, cateto2:float):#->float:
##    suma_cuadrados = (cateto1**2)+(cateto2**2)
##    hipotenusa = pow(suma_cuadrados, 0.5)
##    return hipotenusa
##
##cadena_cat_1 = input("Indique la longitud del primer cateto: ")
##cadena_cat_2 = input("Indique la longitud del segundo cateto: ")
##cat_1 = float(cadena_cat_1)
##cat_2 = float(cadena_cat_2)
##perimetro = perimetro_triangulo(cat_1,cat_2)
##print("El perímetro de un triángulo rectángulo que tenga catetos de longitud",cat_1,"y",cat_2,"es",perimetro)

#Parte 5.3
##def perimetro_triangulo ( cateto1, cateto2):#->float: 
##    hipotenusa = calcular_hip(cateto1, cateto2)
##    return cateto1+cateto2+hipotenusa
##
##def calcular_hip(cateto1, cateto2):#->float:
##    suma_cuadrados = (cateto1**2)+(cateto2**2)
##    hipotenusa = pow(suma_cuadrados, 0.5)
##    return hipotenusa
##
##cadena_cat_1 = float(input("Indique la longitud del primer cateto: "))
##cadena_cat_2 = float(input("Indique la longitud del segundo cateto: "))
##cat_1 = float(cadena_cat_1)
##cat_2 = float(cadena_cat_2)
##perimetro = perimetro_triangulo(cat_1,cat_2)
##print("El perímetro de un triángulo rectángulo que tenga catetos de longitud",cat_1,"y",cat_2,"es",perimetro)

#Parte 5.4
##def perimetro_triangulo ( cateto1:float, cateto2:float)->float: 
##    hipotenusa = calcular_hip(cateto1, cateto2)
##    return cateto1+cateto2+hipotenusa
##
##def calcular_hip(cateto1:float, cateto2:float)->float:
##    suma_cuadrados = (cateto1**2)+(cateto2**2)
##    hipotenusa = pow(suma_cuadrados, 0.5)
##    return hipotenusa
##
##cadena_cat_1 = input("Indique la longitud del primer cateto: ")
##cadena_cat_2 = input("Indique la longitud del segundo cateto: ")
##cat_1 = float(cadena_cat_1)
##cat_2 = float(cadena_cat_2)
##perimetro = perimetro_triangulo(cat_1,cat_2)
##print("El perímetro de un triángulo rectángulo que tenga catetos de longitud",cat_1,"y",cat_2,"es",perimetro)


#Parte 6
##def area_perimtero_rectangulo(base, altura):
##    perimetro = 2*base + 2*altura
##    area = base * altura
##    return perimetro, area
##
##bas = float(input("Ingrese la base del rectangulo "))
##alt = float(input("Ingrese la altura del rectangulo "))
##perimetro, area = area_perimtero_rectangulo(bas, alt)
##print("Perimetro: ", perimetro, "Area: ", area)


#Parte 7


