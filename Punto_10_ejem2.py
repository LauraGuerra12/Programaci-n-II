'''Diseñe un algoritmo empleando la programación orientada a objetos con Python para resolver el problema mostrado en la siguiente imagen. Se presenta un diagrama de clases para vehículos con atributos especificados. Cree los métodos necesarios para permitir ingresar vehículos en las diferentes clases y poder mostrar la información contenida en ellos. Adicional cree al menos 2 métodos para cada clase que usted considere importantes y necesarios en la ejecución del mismo. Su programa debe tener menús de acceso y permitir: agregar, editar y borrar información. '''

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas  

    def mostrar_info(self):
        return (f"Color: {self.color}, Ruedas: {self.ruedas}") 
    
    def editar_info(self, color=None, ruedas=None):
        if color:
            self.color = color
        if ruedas:
            self.ruedas = ruedas

    def __str__(self):
        return self.mostrar_info()
    
class Automovil(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindraje):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindraje = cilindraje

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Velocidad: {self.velocidad} km/h, Cilindraje: {self.cilindraje} cc"

    def editar_info(self, velocidad=None, cilindraje=None, **kwargs):
        super().editar(**kwargs)
        if velocidad:
            self.velocidad = velocidad
        if cilindraje:
            self.cilindraje = cilindraje
    
class Camioneta(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindraje, carga):
        super().__init__(color, ruedas, velocidad, cilindraje)
        self.carga = carga

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Velocidad: {self.velocidad} km/h, Cilindraje: {self.cilindraje} cc, Carga: {self.carga} kg"

    def editar_info(self, velocidad=None, cilindraje=None, carga=None, **kwargs):
        super().editar(**kwargs)
        if velocidad:
            self.velocidad = velocidad
        if cilindraje:
            self.cilindraje = cilindraje
        if carga:
            self.carga = carga 

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Tipo: {self.tipo}"

    def editar_info(self, tipo=None, **kwargs):
        super().editar(**kwargs)
        if tipo:
            self.tipo = tipo 

class Motocicleta(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindraje):
        super().__init__(color, ruedas, velocidad, cilindraje)
    
class SistemaVehiculos:
    def __init__(self):
        self.vehiculos = []
        
    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def eliminar_vehiculo(self, indice):
        if 0 <= indice < len(self.vehiculos):
            del self.vehiculos[indice]
            return True
        return False

    def mostrar_vehiculos(self):
        for idx, vehiculo in enumerate(self.vehiculos):
            print(f"Índice: {idx} - {vehiculo}")

    def editar_vehiculo(self, indice, **kwargs):
        if 0 <= indice < len(self.vehiculos):
            self.vehiculos[indice].editar(**kwargs)
            return True
        return False

def menu():
    sistema = SistemaVehiculos()
    while True:
        print("\n--- MENÚ ---\n")
        print("1. Agregar Vehículo")
        print("2. Mostrar Vehículos")
        print("3. Editar Vehículo")
        print("4. Eliminar Vehículo")
        print("5. Salir")
        opcion = input("\nSeleccione una opción: ")
        print('')
        print('-'*30)
        print('')

        if opcion == "1":
            tipo = input("Tipo de vehículo (automóvil, camioneta, bicicleta, motocicleta): ").strip().lower()
            color = input("Color: ")
            ruedas = int(input("Número de ruedas: "))

            if tipo == "coche":
                velocidad = float(input("Velocidad (km/h): "))
                cilindraje = int(input("cilindraje (cc): "))
                sistema.agregar_vehiculo(Automovil(color, ruedas, velocidad, cilindraje))
            elif tipo == "camioneta":
                velocidad = float(input("Velocidad (km/h): "))
                cilindraje = int(input("cilindraje (cc): "))
                carga = int(input("Capacidad de carga (kg): "))
                sistema.agregar_vehiculo(Camioneta(color, ruedas, velocidad, cilindraje, carga))
            elif tipo == "bicicleta":
                tipo_bicicleta = input("Tipo (urbana/deportiva): ")
                sistema.agregar_vehiculo(Bicicleta(color, ruedas, tipo_bicicleta))
            elif tipo == "motocicleta":
                velocidad = float(input("Velocidad (km/h): "))
                cilindraje = int(input("cilindraje (cc): "))
                sistema.agregar_vehiculo(Motocicleta(color, ruedas, velocidad, cilindraje))
            else:
                print("Tipo de vehículo no válido.")

        elif opcion == "2":
            sistema.mostrar_vehiculos()

        elif opcion == "3":
            indice = int(input("Ingrese el índice del vehículo a editar: "))
            color = input("Nuevo color (dejar en blanco para no cambiar): ")
            ruedas = input("Nuevo número de ruedas (dejar en blanco para no cambiar): ")

            if ruedas:
                ruedas = int(ruedas)

            kwargs = {"color": color or None, "ruedas": ruedas or None}

            tipo = type(sistema.vehiculos[indice]).__name__
            if tipo == "Coche" or tipo == "Camioneta" or tipo == "Motocicleta":
                velocidad = input("Nueva velocidad (km/h): ")
                cilindraje = input("Nueva cilindraje (cc): ")
                kwargs.update({"velocidad": float(velocidad) if velocidad else None, "cilindraje": int(cilindraje) if cilindraje else None})
                if tipo == "Camioneta":
                    carga = input("Nueva carga (kg): ")
                    kwargs["carga"] = int(carga) if carga else None
            elif tipo == "Bicicleta":
                tipo_bicicleta = input("Nuevo tipo (urbana/deportiva): ")
                kwargs["tipo"] = tipo_bicicleta or None

            if sistema.editar_vehiculo(indice, **kwargs):
                print("Vehículo editado con éxito.")
            else:
                print("Índice inválido.")

        elif opcion == "4":
            indice = int(input("Ingrese el índice del vehículo a eliminar: "))
            if sistema.eliminar_vehiculo(indice):
                print("Vehículo eliminado con éxito.")
            else:
                print("Índice inválido.")

        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()