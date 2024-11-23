'''Diseñe un programa aplicando POO para un concesionario de autos (automóviles, camionetas, camiones, tractocamiones), tenga en cuenta las características en común y cree las clases necesarias, por ejemplo modelos, tipo de pintura, cantidades de unidades en inventario. '''

class Vehiculo:
    def __init__(self, modelo, marca, año, tipo_pintura, precio, cantidad):
        self.modelo = modelo
        self.marca = marca
        self.año = año
        self.tipo_pintura = tipo_pintura
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_info(self):
        return (f"Modelo: {self.modelo}, Marca: {self.marca}, Año: {self.año}, "
                f"Pintura: {self.tipo_pintura}, Precio: ${self.precio}, Cantidad: {self.cantidad}")

class Automovil(Vehiculo):
    def __init__(self, modelo, marca, año, tipo_pintura, precio, cantidad):
        super().__init__(modelo, marca, año, tipo_pintura, precio, cantidad)

class Camioneta(Vehiculo):
    def __init__(self, modelo, marca, año, tipo_pintura, precio, cantidad):
        super().__init__(modelo, marca, año, tipo_pintura, precio, cantidad)

class Camion(Vehiculo):
    def __init__(self, modelo, marca, año, tipo_pintura, precio, cantidad):
        super().__init__(modelo, marca, año, tipo_pintura, precio, cantidad)

class Tractocamion(Vehiculo):
    def __init__(self, modelo, marca, año, tipo_pintura, precio, cantidad):
        super().__init__(modelo, marca, año, tipo_pintura, precio, cantidad)

class Inventario:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def mostrar_inventario(self):
        print("\nInventario de Vehículos:")
        for vehiculo in self.vehiculos:
            print(vehiculo.mostrar_info())

    def buscar_por_tipo(self, tipo):
        return [v for v in self.vehiculos if v.__class__.__name__ == tipo]

    def contar_vehiculos_por_tipo(self):
        conteo = {"Automovil": 0, "Camioneta": 0, "Camion": 0, "Tractocamion": 0}
        for vehiculo in self.vehiculos:
            conteo[vehiculo.__class__.__name__] += vehiculo.cantidad
        return conteo

def menu():
    inventario = Inventario()
    
    while True:
        print("\n--- Concesionario de Vehículos ---\n")
        print("1. Agregar Automóvil")
        print("2. Agregar Camioneta")
        print("3. Agregar Camión")
        print("4. Agregar Tractocamión")
        print("5. Mostrar Inventario")
        print("6. Buscar Vehículos por Tipo")
        print("7. Contar Vehículos por Tipo")
        print("8. Salir")
        opcion = input("\nSeleccione una opción: ")
        print("")
        print("-" * 30)
        print("")
        
        if opcion == "1":
            agregar_vehiculo(inventario, "Automovil")

        elif opcion == "2":
            agregar_vehiculo(inventario, "Camioneta")

        elif opcion == "3":
            agregar_vehiculo(inventario, "Camion")

        elif opcion == "4":
            agregar_vehiculo(inventario, "Tractocamion")

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            tipo = input("Ingrese el tipo de vehículo a buscar (Automovil, Camioneta, Camion, Tractocamion): ")
            vehiculos_tipo = inventario.buscar_por_tipo(tipo)
            print(f"\nVehículos de tipo {tipo}:")
            for vehiculo in vehiculos_tipo:
                print(vehiculo.mostrar_info())

        elif opcion == "7":
            conteo = inventario.contar_vehiculos_por_tipo()
            print("\nConteo de Vehículos por Tipo:")
            for tipo, cantidad in conteo.items():
                print(f"{tipo}: {cantidad}")

        elif opcion == "8":
            print("Saliendo del programa...")
            exit()
        else:
            print("Opción no válida. Intente de nuevo.")

def agregar_vehiculo(inventario, tipo_vehiculo):
    marca = input("Ingrese la marca: ")
    modelo = input("Ingrese el modelo: ")
    año = int(input("Ingrese el año: "))
    tipo_pintura = input("Ingrese el tipo de pintura: ")
    precio = float(input("Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad de unidades en inventario: "))

    if tipo_vehiculo == "Automovil":
        vehiculo = Automovil(marca, modelo, año, tipo_pintura, precio, cantidad)
    elif tipo_vehiculo == "Camioneta":
        vehiculo = Camioneta(marca, modelo, año, tipo_pintura, precio, cantidad)
    elif tipo_vehiculo == "Camion":
        vehiculo = Camion(marca, modelo, año, tipo_pintura, precio, cantidad)
    elif tipo_vehiculo == "Tractocamion":
        vehiculo = Tractocamion(marca, modelo, año, tipo_pintura, precio, cantidad)

    inventario.agregar_vehiculo(vehiculo)
    print(f"{tipo_vehiculo} agregado al inventario con éxito.")

menu()