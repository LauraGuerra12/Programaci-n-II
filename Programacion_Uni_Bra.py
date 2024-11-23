import csv
materias=[]

estudiantes={"Laura":{"contraseña": "1234"}, "Felipe":{"contraseña":"1235"}, "Juan":{"contraseña":"1236"}}
admin={"admi":{"contraseña": "0000"}}
docentes={"docente1":{"contraseña": "1525"}, "docente2": {"contraseña": "1235"}}
e="si"

def menu():
    a=int(input('''Bienvenidos a la pagina de la U
                        desea ingresar como:
                            1 administrador
                            2 estudiante
                            3 profesor\n'''))
    match a:
        case 1:
            administrador()
        case 2:
            estudiantes()
        case 3:
            profesor()

def administrador():
    a="si"
    while a=="si":
        usuario=input("Por favor ingrese su nombre de usuario\n")
        if usuario in admin:
            passw=input("Ingrese su contraseña\n")
            if passw == admin[usuario]["contraseña"]:
                b=int(input('''Has ingreasado como administrador marca
                        1 Si deseas hacer deseas hacer modificaciones al sistema
                        2 Si solo deseas revisar el sistema\n'''))
                match b:
                    case 1:
                        configuracion_admi()
                    case 2:
                        revision()
                                                      
            else:
                a=input("Contraseña es incorrecta si desea volver a ingresar marque 'si'\n")
        else:
            a=input("Usuario es erroneo si debeas volver a intentar marca 'si'\n")

def configuracion_admi():
    c=int(input('''Has marcado la opcion para hacer modificaciones elige la opcion que deseas realizar
                        1 Registrar nuevos estudiante
                        2 Registrar la materias
                        3 Registrar libros\n'''))
    match c:
        case 1:
            nuevos_est()
        case 2:
            regis_materias()
        case 3:
            regis_libros()


def nuevos_est():
    n=int(input("cuantos estudiantes desea ingresar"))
    for i in range(n):
        nombre=input('por favor ingrese el nombre del nuevo estudiante que desea registrar\n')
        contraseña=input('por favor ingrese la contraseña del estudiante\n')
        estudiantes[nombre] = {"contraseña": contraseña}
        print(f'El estudiante {nombre} ha sido registrado exitosamente.\n')
    e="si"
    while e=="si":
        try:
            d=int(input('''ya has ingresado exitosamente a los estudiantes deseas
                                1 volver a menu
                                2 volver a configuraciones'''))
            match d:
                case 1:
                    menu()
                case 2:
                    configuracion_admi()
        except:
            e=input("Ha ocurrido un error al marcar, recuerda que tiene que ser tipo entero deseas volver marca 'si' ")

def regis_materias():
    n=int(input("Cuantas materias deseas ingresar: \n"))
    for i in range(n):
        codi=input(f'ingrese el codigo de la materia que va a registrar\n')
        asig=input(f'ingrese la materia que va a registar\n')
        print(f'la materia {asig} ha sido registrada exitosamente')
        materias.append([codi,asig])
    return escribir_csv()

def escribir_csv():
    with open('c:/Users/Brayan David/Desktop/materias.csv', 'w', newline='') as pou:
        escri=csv.writer(pou, delimiter=';')
        escri.writerows(materias)
    print("se ha registrado exitosamente las materias marca1")
##    match h:
##        case 1:
##            ver()
##    
##def ver():
##    l=input('deseas ver las materias registradas')
##    while l>0:
##        with open('C:/Users/Brayan David/Desktop/materias.csv',  newline='') as pou:
##            leer=csv.reader(pou, delimiter=';')        #Lector del csv
##            materias=list(leer)
##        if l==1:
##            for i in materias:
##                print(i) 
##    
        
                 
menu()           
        
