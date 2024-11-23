#Diseñar un algoritmo que nos permita tener dos usuarios: profesores y estudiantes
#Profesor: registrar notas de asignaturas, autenticarse con usuario y contraseña
#Estudiante: solo puede ver las notas, pero debe autenticarse con usuario y contraseña
#Asignaturas: 2 para cada profesor
#Prueba del algoritmo: 2 profes, 4 asignaturas, 5 estudiantes
#Requisito: los datos deben quedar almacenados en un archivo CSV


import csv
profes = {"hector":1234, "jeider":4321}
#estu1 = ["laura", 1010 "daniel", 1011 "jhon", 1012, "juan", 1013, "nicolas", 1014]   Una opcion de lista, pero puede ser un poco mas enredada
estu = ["laura", "daniel", "jhon", "juan", "nicolas"]
contra = [1010, 1011, 1012, 1013, 1014]
aignatura = ["calculo", "programacion", "dibujo", "circuitos"]
notas = [[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]]

def profesor ():
    usu = input('Ingrese su usuario: ').lower()
    clave = int(input('Ingrese su contraseña: '))
    if (usu in profes) == True and (profes[usu]) == clave:
        print('Usuario autenticado')
    else:
        print('Error de usuario y/o contraseña')
    

    menu()



    
def menu():
    print("""Bienvenido al programa de notas UIS Barbosa
            Marque: 1. Profesor
                    2. Estudiante""")
    ingreso = int(input("opción\n"))
    if ingreso == 1:
        print("Bienvenido profesor")
        profesor()    #me dirige a la función profesor
        
    elif ingreso == 2:
        print("Bienvenido estudiante")
    else:
        print("Error de opción")



menu()
