'''Una empresa lo contrata para crear un algoritmo gestor que pueda manejar toda la información de un cinema. Se debe gestionar: El cinema exige una interfaz gráfica para sus empleados y usuarios (clientes), Cartelera de películas (nombre de la película y horario, mostrar en interfaz), Compra de tiquetes (permitir llevar el control de que película compran tiquetes y almacenar la información), Venta de comidas (mostrar en interfaz y almacenar la información) e Informe para administrador: Numero de tiquetes vendidos en cada película, dinero ganado por películas y venta de comida. Todos los registros deben quedar almacenados en archivo CSV.'''


import csv

def crear_archivo(archivo, nombre, columnas):
    with open(archivo, 'w') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(columnas)
        return archivo

def leer_archivo(archivo):
    with open(archivo, 'r') as archivo:
        reader = csv.reader(archivo)
        return reader

def leer_columnas(archivo):
    with open(archivo, 'r') as archivo:
        reader = csv.reader(archivo)
        return reader.next()

def leer_registros(archivo):
    with open(archivo, 'r') as archivo:
        reader = csv.reader(archivo)
        return reader.next()

def escribir_registro(archivo, registro):
    with open(archivo, 'a') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(registro)

def actualizar_registro(archivo, registro, fila):
    with open(archivo, 'r') as archivo:        
        reader = csv.reader(archivo)
        registros = list(reader)
    
    with open(archivo, 'w') as archivo:
        writer = csv.writer(archivo)
        for idx, reg in enumerate(registros):
            if idx == fila:
                writer.writerow(registro)
            else:
                writer.writerow(reg)                                

class Cinema:
    def __init__(self, nombre, direccion, horarios):
        self.nombre = nombre
        self.direccion = direccion
        self.horarios = horarios
        self.tiquetes_vendidos = {}
        self.comida_vendida = {}
        self.dinero_ganado = 0

    def mostrar_info(self):
        return f"Nombre: {self.nombre}\nDirección: {self.direccion}\nHorarios: {self.horarios}\nTiquetes vendidos: {self.tiquetes_vendidos}\nComida vendida: {self.comida_vendida}\nDinero ganado: {self.dinero_ganado}"

    def agregar_tiquetes(self, pelicula, cantidad):
        if pelicula in self.tiquetes_vendidos:
            self.tiquetes_vendidos[pelicula] += cantidad
        else:
            self.tiquetes_vendidos[pelicula] = cantidad

    def agregar_comida(self, pelicula, cantidad):
        if pelicula in self.comida_vendida:
            self.comida_vendida[pelicula] += cantidad
        else:
            self.comida_vendida[pelicula] = cantidad

    def calcular_dinero(self, pelicula):
        if pelicula in self.comida_vendida:
            self.dinero_ganado += self.comida_vendida[pelicula] * 5

    def __str__(self):
        return self.mostrar_info()

class CinemaAdmin:
    def __init__(self, cinemas):
        self.cinemas = cinemas

    def mostrar_info(self):
        for cinema in self.cinemas:
            print(cinema)

    def agregar_cinema(self, nombre, direccion, horarios):
        self.cinemas.append(Cinema(nombre, direccion, horarios))

    def eliminar_cinema(self, indice):
        if 0 <= indice < len(self.cinemas):
            del self.cinemas[indice]
            return True
        return False

    def mostrar_tiquetes(self, indice):
        if 0 <= indice < len(self.cinemas):
            print(self.cinemas[indice].mostrar_info())
            return True
        return False

    def agregar_tiquetes(self, indice, pelicula, cantidad):
        if 0 <= indice < len(self.cinemas):
            self.cinemas[indice].agregar_tiquetes(pelicula, cantidad)
            return True
        return False

    def agregar_comida(self, indice, pelicula, cantidad):
        if 0 <= indice < len(self.cinemas):
            self.cinemas[indice].agregar_comida(pelicula, cantidad)
            return True
        return False

    def calcular_dinero(self, indice, pelicula):
        if 0 <= indice < len(self.cinemas):
            self.cinemas[indice].calcular_dinero(pelicula)
            return True
        return False

def menu():
    cinemas = []
    while True:
        print("\n--- MENÚ ---\n")
        print("1. Agregar Cinema")
        print("2. Mostrar Cinemas")
        print("3. Agregar Tiquetes")
        print("4. Agregar Comida")
        print("5. Calcular Dinero")
        print("6. Salir")
        opcion = input("\nSeleccione una opción: ")
        print('')
        print('-'*30)
        print('')

        if opcion == "1":
            nombre = input("Nombre del cinema: ")
            direccion = input("Dirección: ")
            horarios = input("Horarios (de la mañana a la noche): ")
            cinemas.append(Cinema(nombre, direccion, horarios))

        elif opcion == "2":
            for cinema in cinemas:
                print(cinema)

        elif opcion == "3":
            indice = int(input("Ingrese el índice del cinema a agregar tiquetes: "))
            pelicula = input("Ingrese la película: ")
            cantidad = int(input("Ingrese la cantidad de tiquetes: "))
            if cinemas[indice].agregar_tiquetes(pelicula, cantidad):
                print("Tiquetes agregados con éxito.")
            else:
                print("Índice inválido.")

        elif opcion == "4":
            indice = int(input("Ingrese el índice del cinema a agregar comida: "))
            pelicula = input("Ingrese la película: ")
            cantidad = int(input("Ingrese la cantidad de comida: "))
            if cinemas[indice].agregar_comida(pelicula, cantidad):
                print("Comida agregada con éxito.")
            else:
                print("Índice inválido.")

        elif opcion == "5":
            indice = int(input("Ingrese el índice del cinema a calcular dinero: "))
            pelicula = input("Ingrese la película: ")
            if cinemas[indice].calcular_dinero(pelicula):
                print("Dinero calculado con éxito.")
            else:
                print("Índice inválido.")

        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()  