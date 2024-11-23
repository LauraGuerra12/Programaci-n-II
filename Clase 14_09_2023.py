import csv

admin = {"admin":1234}
profes = {}
estudiantes = {}
asignaturas = []


def Academico():
    print("acad")
    h_usuarios = int(intput("Marque 1.Pofes 2.Estudiantes 3.Asignaturas"))
    if h_usuarios == 1:
         usu = input("Ingrese el nuevo usuario_ ")
         contra = int(input('Ingrese la contraseña para el nuevo usuario'))
         profes[usu]=contra
         print('Usuario Almacenado')
         Academino()
     
        


    
    

def Convivencia():
    print("Convivencia")

def Biblioteca():
    print("biblioteca")

def Votaciones():
    print("votaciones")

def Acceso():
    print("Bienvenido al menú de acceso: 1. Administrativo. 2. Profesor. 3. Estudiante")
    opcion = int(input())
    if opcion == 1:
        Print("Bienvenido Admin")
        usu = input("Ingrese su usuario: ")
        contra = int(input( "Ingrese su contraseña: "))
        if usu in admin and contra == admin[usu]:
            print ("Ok")
            modulo = int(intput("A que modulo quiere ir"))
            if modulo == 1:
                Academico()
            elif modulo == 2:
                Concivencia()
            elif modulo == 3:
                Votaciones()
            elif modulo == 4:
                Biblioteca()
            else:
                print("Dato erroneo")
                
        else:
            print("Dato erroneo")

Acceso()
        
                     
