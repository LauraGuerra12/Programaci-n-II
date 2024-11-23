import csv
from datetime import datetime
from datetime import timedelta

placas=[]
tiempoV={}
tiempoM={}

def menu():
##    with open('C:/Users/Brayan David/Desktop/parqueaderoo.csv', newline=' ') as pool:
##        leer=csv.reader(pool, delimiter=';')
##        placas=list(leer)
    
    a=int(input('''bienvenidos al parqueadero elige una de las opciones
                    1. ingresa vehiculo
                    2. salida de vehiculo
                    3. ingresa moto
                    4. salida moto
                    5. ver registro de los carros ingresados'''))
    match a:
        case 1:
            ingr_v()
        case 2:
            salida_v()
        case 3:
            ingr_m()
        case 4:
            salida_m()
        case 5:
            ver()
        case 6:
            buscar()
            

def ingr_v():
    plac_V=input('por favor la placa de vehiculo que acaba de ingresar\n')
    now=datetime.now()
    print('el vehiculo ingreso ',now)
    tiempoV[plac_V]={'tiempo':now}
    placas.append([plac_V, now])
    return escribir()

def escribir():
    with open('C:/Users/Brayan David/Desktop/parqueaderoo.csv', 'w', newline='') as poo:
        escri=csv.writer(poo, delimiter=';')
        escri.writerows(placas)
    menu()

def ver():
    with open('C:/Users/Brayan David/Desktop/parqueaderoo.csv', newline='') as pool:
        leer=csv.reader(pool, delimiter=';')
        placas=list(leer)
        for i in placas:
            print(i)
    menu()
    
def buscar():
    with open('C:/Users/Brayan David/Desktop/parqueaderoo.csv', newline='') as pool:
        leer=csv.reader(pool, delimiter=';')
        placas=list(leer)
    contador=-1
    a=input('ingrese la placa que desea buscar\n')
    for i in placas:
        contatador=contador+1
        if i[0]==a:
            print(i)
            

        else:
            print('buscando')

    
    
def salida_v():
    plac_vs=input("ingrese las placas del vehiculo que va a salir\n")
    if plac_vs in tiempoV:
        now2=datetime.now()
        print('La hora de entrada es', tiempoV[plac_vs]['tiempo'], 'y la hora de salida es', now2)
        new_date = now2 - tiempoV[plac_vs]['tiempo']
        new_dateS= new_date.seconds
        p=new_dateS/60
        print('Ha durado un tiempo restante de', new_date, 'y tiene un precio de ',p*2)
        
    else:
        print('el vehiculo no ha entrado al garaje')
    menu()


def ingr_m():
    plac_M=input('ingrese la placa de la moto que ingreso\n')
    now3=datetime.now()
    print('la moto ingreso a la hora ', now3)
    tiempoM[plac_M]={'tiempo':now3}
    menu()

def salida_m():
    plac_ms=input('ingrese la placa de la moto que va a salir\n')
    if plac_ms in tiempoM:
        now4=datetime.now()
        print('La hora de entrada es', tiempoM[plac_ms]['tiempo'], 'y la hora de salida es', now4)
        new_date = now2 - tiempoM[plac_ms]['tiempo']
        print('Ha durado un tiempo restante de', new_date)
    else:
        print('la moto ')
    menu()
menu()
