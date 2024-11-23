#Punto 1
##def area_perimtero_rectangulo(base, altura):
##    perimetro = 2*base + 2*altura
##    area = base * altura
##    return perimetro, area
##
##bas = float(input("Ingrese la base del rectangulo "))
##alt = float(input("Ingrese la altura del rectangulo "))
##perimetro, area = area_perimtero_rectangulo(bas, alt)
##print("Perimetro: ", perimetro, "Area: ", area)


#Punto 2



#Punto 3



#Punto 4



#Punto 5
def Suma():
    a = float(input("Numero "))
    b = float(input("Numero "))
    print(a+b)
    menu()
    
def Resta():
    a = float(input("Numero "))
    b = float(input("Numero "))
    print(a-b)
    menu()

def Producto():
    a = float(input("Numero "))
    b = float(input("Numero "))
    print(a*b)
    menu()

def Cociente():
    a = float(input("Numero "))
    b = float(input("Numero "))
    print(a/b)
    menu()

def menu(): #Esta es la funcion principal
    print('''Seleccione:             1:Suma
                        2:Diferencia
                        3:Producto
                        4:Cociente
                        5:Salir''')
    op = int(input("Opcion deseada "))
    while op>=1 and op<=5:
        if op == 1:
            Suma()
        elif op == 2:
            Resta()
        elif op == 3:
            Producto()
        elif op == 4:
            Cociente()
        elif op == 5:
            exit()
        else:
            print("Error")
menu()
    
