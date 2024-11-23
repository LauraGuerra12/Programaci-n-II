'''Una familia quiere digitalizar el árbol genealógico, están dispuestos a contratar un ingeniero que les haga un programa donde ellos puedan almacenar la información: nombres, apellidos, edad, género y generación (bisabuelos, abuelos, padres, yo, hijos). Teniendo en cuenta los parámetros dados por la familia. Usted debe hacer un programa empleando POO en Python. En una clase llamada Persona () se pueden ingresar los datos básicos (nombre, apellido, edad y genero) de los familiares, según criterio de edad él pueda ubicarse en la Clase Generación () correspondiente y cuando desee mostrar en pantalla su árbol genealógico pueda hacerse: ascendente o descendente cronológicamente y aparecer todos los datos de la persona.'''

class Persona:
    def __init__(self, nombre, apellido, edad, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero
        self.generacion = None  # Se asignará en la clase Generacion

    def mostrar_info(self):
        return (f"{self.nombre} {self.apellido}, Edad: {self.edad}, Género: {self.genero}, Generación: {self.generacion}")

class Generacion:
    def __init__(self):
        self.personas = {
            "Bisabuelos": [],
            "Abuelos": [],
            "Padres": [],
            "Yo": [],
            "Hijos": []
        }

    def agregar_persona(self, persona):
        if persona.edad >= 80:
            generacion = "Bisabuelos"
        elif 60 <= persona.edad < 80:
            generacion = "Abuelos"
        elif 40 <= persona.edad < 60:
            generacion = "Padres"
        elif 20 <= persona.edad < 40:
            generacion = "Yo"
        else:
            generacion = "Hijos"
        
        persona.generacion = generacion
        self.personas[generacion].append(persona)
        print(f"{persona.nombre} {persona.apellido} agregado a la generación: {generacion}")

    def mostrar_arbol_ascendente(self):
        print("\n--- Árbol Genealógico en Orden Ascendente ---")
        for generacion in ["Hijos", "Yo", "Padres", "Abuelos", "Bisabuelos"]:
            if self.personas[generacion]:
                print(f"\n{generacion}:")
                for persona in self.personas[generacion]:
                    print(persona.mostrar_info())

    def mostrar_arbol_descendente(self):
        print("\n--- Árbol Genealógico en Orden Descendente ---\n")
        for generacion in ["Bisabuelos", "Abuelos", "Padres", "Yo", "Hijos"]:
            if self.personas[generacion]:
                print(f"\n{generacion}:")
                for persona in self.personas[generacion]:
                    print(persona.mostrar_info())

def menu():
    arbol_genealogico = Generacion()

    while True:
        print("\n--- Menú Árbol Genealógico ---\n")
        print("1. Agregar Persona")
        print("2. Mostrar Árbol Genealógico Ascendente")
        print("3. Mostrar Árbol Genealógico Descendente")
        print("4. Salir")
        opcion = input("\nSeleccione una opción: ")
        print('')
        print('-'*30)        
        print('')

        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            edad = int(input("Ingrese la edad: "))
            genero = input("Ingrese el género (M/F): ")
            persona = Persona(nombre, apellido, edad, genero)
            arbol_genealogico.agregar_persona(persona)

        elif opcion == "2":
            arbol_genealogico.mostrar_arbol_ascendente()

        elif opcion == "3":
            arbol_genealogico.mostrar_arbol_descendente()

        elif opcion == "4":
            print("Saliendo del sistema...")
            exit()

        else:
            print("Opción no válida. Intente de nuevo.")

menu()