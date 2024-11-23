'''
Diseñe un programa para un zoológico, por medio de clases y objetos. Su programa debe permitir almacenar información de animales por especies
(terrestre, aéreos y acuáticos) y las características de cada uno por especie. Aclaración: Cuando se ejecuta el programa debe preguntar que especie 
de animal desea ingresar, según su selección haremos una clase para cada especie y el objeto que se cree solicita las características pertinentes. 
'''

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_info(self):
        pass  # Método que será implementado en cada subclase.


class Terrestre(Animal):
    def __init__(self, nombre, patas, pulmones, piel, cuerpo, sentidos):
        super().__init__(nombre)
        self.patas = patas
        self.pulmones = pulmones
        self.piel = piel
        self.cuerpo = cuerpo
        self.sentidos = sentidos

    def mostrar_info(self):
        print(f"Animal Terrestre: {self.nombre}")
        print(f"Patas: {self.patas}")
        print(f"Pulmones: {self.pulmones}")
        print(f"Piel: {self.piel}")
        print(f"Cuerpo: {self.cuerpo}")
        print(f"Sentidos: {self.sentidos}")


class Acuatico(Animal):
    def __init__(self, nombre, aletas, respiracion, piel, flotabilidad, sentidos):
        super().__init__(nombre)
        self.aletas = aletas
        self.respiracion = respiracion
        self.piel = piel
        self.flotabilidad = flotabilidad
        self.sentidos = sentidos

    def mostrar_info(self):
        print(f"Animal Acuático: {self.nombre}")
        print(f"Aletas: {self.aletas}")
        print(f"Respiración: {self.respiracion}")
        print(f"Piel: {self.piel}")
        print(f"Flotabilidad: {self.flotabilidad}")
        print(f"Sentidos: {self.sentidos}")


class Aereo(Animal):
    def __init__(self, nombre, alas, cuerpo, plumas, vision, pulmones):
        super().__init__(nombre)
        self.alas = alas
        self.cuerpo = cuerpo
        self.plumas = plumas
        self.vision = vision
        self.pulmones = pulmones

    def mostrar_info(self):
        print(f"Animal Aéreo: {self.nombre}")
        print(f"Alas: {self.alas}")
        print(f"Cuerpo: {self.cuerpo}")
        print(f"Plumas: {self.plumas}")
        print(f"Visión: {self.vision}")
        print(f"Pulmones: {self.pulmones}")


def crear_animal():
    print("Seleccione la especie de animal que desea ingresar:")
    print("1. Terrestre")
    print("2. Acuático")
    print("3. Aéreo")
    
    opcion = input("Ingrese el número de la especie: ")

    nombre = input("Nombre del animal: ")

    if opcion == "1":
        patas = input("Número de patas: ")
        pulmones = input("Descripción de los pulmones: ")
        piel = input("Tipo de piel o pelaje: ")
        cuerpo = input("Descripción del cuerpo: ")
        sentidos = input("Descripción de los sentidos adaptados: ")
        animal = Terrestre(nombre, patas, pulmones, piel, cuerpo, sentidos)
        
    elif opcion == "2":
        aletas = input("Descripción de aletas o cuerpo hidrodinámico: ")
        respiracion = input("Método de respiración (branquias o pulmones especializados): ")
        piel = input("Tipo de piel o escamas: ")
        flotabilidad = input("Capacidad de regular la flotabilidad: ")
        sentidos = input("Descripción de los sentidos adaptados al agua: ")
        animal = Acuatico(nombre, aletas, respiracion, piel, flotabilidad, sentidos)
        
    elif opcion == "3":
        alas = input("Descripción de las alas o membranas: ")
        cuerpo = input("Descripción del cuerpo (ligero o huesos huecos): ")
        plumas = input("Descripción de las plumas o piel ligera: ")
        vision = input("Descripción de la visión: ")
        pulmones = input("Descripción de los pulmones con sacos aéreos: ")
        animal = Aereo(nombre, alas, cuerpo, plumas, vision, pulmones)
        
    else:
        print("Opción no válida.")
        return None

    return animal


def main():
    animales = []

    while True:
        print("\n--- Registro de Animales en el Zoológico ---")
        animal = crear_animal()
        if animal:
            animales.append(animal)
            print("\nAnimal registrado con éxito.\n")
        
        continuar = input("¿Desea registrar otro animal? (s/n): ")
        if continuar.lower() != 's':
            break

    print("\n--- Información de los Animales Registrados ---")
    for animal in animales:
        animal.mostrar_info()
        print("\n")


if __name__ == "__main__":
    main()
