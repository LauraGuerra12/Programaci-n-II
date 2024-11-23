'''Diseñe un algoritmo empleando Python, POO y sus propiedades (herencia, encapsulamiento y polimorfismo) en la solución de un problema que involucre la ingeniería electrónica. Puede buscar una asignatura de su pensum para realizar una aplicación.'''

class Componente:
    def __init__(self, valor):
        self._valor = valor  # Atributo de valor del componente

class Resistencia(Componente):
    def calcular_total(self, componentes, configuracion):
        if configuracion == "serie":
            return sum([componente._valor for componente in componentes])
        elif configuracion == "paralelo":
            try:
                return 1 / sum([1 / componente._valor for componente in componentes])
            except ZeroDivisionError:
                return "Error: resistencia infinita en paralelo con una resistencia cero."

class Capacitancia(Componente):
    def calcular_total(self, componentes, configuracion):
        if configuracion == "serie":
            try:
                return 1 / sum([1 / componente._valor for componente in componentes])
            except ZeroDivisionError:
                return "Error: capacitancia infinita en serie con una capacitancia cero."
        elif configuracion == "paralelo":
            return sum([componente._valor for componente in componentes])

class Inductancia(Componente):
    def calcular_total(self, componentes, configuracion):
        if configuracion == "serie":
            return sum([componente._valor for componente in componentes])
        elif configuracion == "paralelo":
            try:
                return 1 / sum([1 / componente._valor for componente in componentes])
            except ZeroDivisionError:
                return "Error: inductancia infinita en paralelo con una inductancia cero."


class Circuito:
    def __init__(self):
        self.componentes = []

    def agregar_componente(self, componente):
        self.componentes.append(componente)

    def calcular_total(self, tipo, configuracion):
        componentes_tipo = [comp for comp in self.componentes if isinstance(comp, tipo)]
        if not componentes_tipo:
            return "No hay componentes de este tipo en el circuito."
        return componentes_tipo[0].calcular_total(componentes_tipo, configuracion)


def menu():
    circuito = Circuito()
    
    while True:
        print("\n--- Circuito Eléctrico ---\n")
        print("1. Agregar Resistencia")
        print("2. Agregar Capacitancia")
        print("3. Agregar Inductancia")
        print("4. Calcular Total de Resistencias")
        print("5. Calcular Total de Capacitancias")
        print("6. Calcular Total de Inductancias")
        print("7. Salir")
        opcion = input("\nSeleccione una opción: ")
        print('')
        print('-'*30)
        print('')

        if opcion == "1":
            valor = float(input("Ingrese el valor de la resistencia en ohmios: "))
            resistencia = Resistencia(valor)
            circuito.agregar_componente(resistencia)
            print("Resistencia agregada.")
        
        elif opcion == "2":
            valor = float(input("Ingrese el valor de la capacitancia en faradios: "))
            capacitancia = Capacitancia(valor)
            circuito.agregar_componente(capacitancia)
            print("Capacitancia agregada.")
        
        elif opcion == "3":
            valor = float(input("Ingrese el valor de la inductancia en henrios: "))
            inductancia = Inductancia(valor)
            circuito.agregar_componente(inductancia)
            print("Inductancia agregada.")
        
        elif opcion == "4":
            configuracion = input("Ingrese la configuración (serie/paralelo): ").lower()
            total = circuito.calcular_total(Resistencia, configuracion)
            print(f"Resistencia Total ({configuracion}): {total} ohmios")
        
        elif opcion == "5":
            configuracion = input("Ingrese la configuración (serie/paralelo): ").lower()
            total = circuito.calcular_total(Capacitancia, configuracion)
            print(f"Capacitancia Total ({configuracion}): {total} faradios")
        
        elif opcion == "6":
            configuracion = input("Ingrese la configuración (serie/paralelo): ").lower()
            total = circuito.calcular_total(Inductancia, configuracion)
            print(f"Inductancia Total ({configuracion}): {total} henrios")
        
        elif opcion == "7":
            print("Saliendo del sistema...")
            exit()
        else:
            print("Opción no válida. Intente de nuevo.")

menu()

