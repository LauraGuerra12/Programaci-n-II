'''Necesito el codigo para que en un salon de clase al ingresar se pongan las huellas digitales (es un lector de huella digital) de los alumnos y del profesor. El sistema debe permitir ingresar el código de la huella digital y mostrar el nombre del alumno y que el unico que tenga acceso para abrir la puerta sea la huella del docente a ciertas horas del dia. Para ello, debe tener un archivo CSV con la información de los alumnos y la huella digital. El archivo debe tener las siguientes columnas: Nombre, Código huella, Hora de apertura, Hora de cierre. Debe poder ingresar el código y ver el nombre del alumno. Realizarlo con clases y objetos, pero que lleve pandas.'''

import  pandas as pd
import re

class Profesor:
    def __init__(self, nombre, codigo_huella, hora_apertura, hora_cierre):
        self.nombre = nombre
        self.codigo_huella = codigo_huella
        self.hora_apertura = hora_apertura
        self.hora_cierre = hora_cierre

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Código huella: {self.codigo_huella}")
        print(f"Hora de apertura: {self.hora_apertura}")
        print(f"Hora de cierre: {self.hora_cierre}")

def validar_codigo(codigo_huella):
    """Valida que el código de la huella sea alfanumérico y tenga exactamente 6 caracteres"""
    if re.fullmatch(r'^[A-Za-z0-9]{6}$', codigo_huella):
        return True
    else:
        print("Código de la huella inválido. Debe ser alfanumérico y tener exactamente 6 caracteres.")
        return False

def validar_hora(hora_apertura, hora_cierre):
    """Valida que la hora sea en formato HH:MM y que la hora de apertura sea anterior a la de cierre"""
    if re.fullmatch(r'^([0-1][0-9]|2[0-3]):[0-5][0-9]$', hora_apertura) and re.fullmatch(r'^([0-1][0-9]|2[0-3]):[0-5][0-9]$', hora_cierre):
        hora_apertura = pd.datetime.strptime(hora_apertura, '%H:%M')
        hora_cierre = pd.datetime.strptime(hora_cierre, '%H:%M')
        if hora_apertura < hora_cierre:
            return True
        else:
            print("La hora de apertura no puede ser posterior a la de cierre.")
            return False

class Alumno:
    def __init__(self, nombre, codigo_huella, hora_ingreso):
        self.nombre = nombre
        self.codigo_huella = codigo_huella
        self.hora_ingreso = hora_ingreso

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Código huella: {self.codigo_huella}")
        print(f"Hora de ingreso: {self.hora_ingreso}")

def validar_codigo(codigo_huella):
    """Valida que el código de la huella sea alfanumérico y tenga exactamente 6 caracteres"""
    if re.fullmatch(r'^[A-Za-z0-9]{6}$', codigo_huella):
        return True
    else:
        print("Código de la huella inválido. Debe ser alfanumérico y tener exactamente 6 caracteres.")
        return False

def validar_hora(hora):
    """Valida que la hora sea en formato HH:MM"""
    if re.fullmatch(r'^([0-1][0-9]|2[0-3]):[0-5][0-9]$', hora):
        return True
    else:
        print("Hora inválida. Debe ser en formato HH:MM.")
        return False

def menu():
    while True:
        print("\n--- Menú del sistema de salón de clase ---\n")
        print("1. Ingresar al salón")
        print("2. Salir del sistema")
        opcion = input("\nSeleccione una opción: ")
        print('\n' + '-'*30 + '\n')

        if opcion == '1':
            codigo_huella = input("Ingrese el código de la huella digital: ")
            alumno = Alumno(input("Ingrese el nombre del alumno: "), codigo_huella)
            
            # Leer el archivo CSV
            df = pd.read_csv('alumnos.csv')
            
            # Buscar alumno en el archivo
            for _, row in df.iterrows():
                if row['Código huella'] == codigo_huella:
                    alumno.mostrar_info()
                    print(f"El alumno {alumno.nombre} tiene acceso al salón.")
                    break
            else:
                print("El código de la huella digital no es válido.")

        elif opcion == '2':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()