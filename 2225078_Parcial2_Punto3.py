'''Design a program using OOP, which can be used for the administration of a zoo where data can be taken from all the animals found in it. Consider characteristics such as: species, age, size, weight, height, date of entry to the zoo, gender, type of food, feeding times, vaccines, diseases. Delimit the number of animals that must be greater than 5 and less than 15 of different species. Instantiate each class with at least 2 objects.

Diseña un programa utilizando POO, que pueda ser utilizado para la administración de un zoológico en donde se puedan tomar datos de todos los animales que se encuentran en él. Considera características como: especie, edad, tamaño, peso, altura, fecha de ingreso al zoológico, género, tipo de alimento, horarios de comida, vacunas, enfermedades. Delimita el número de animales que debe ser mayor a 5 y menor a 15 de especies diferentes. Instancía cada clase con al menos 2 objetos.'''

class L_Animal:
    def __init__(self, nombre, edad, tamaño, peso, altura, fecha, genero, tipo_de_alimento, horarios_de_comida, vacunas, enfermedades):
        self.nombre = nombre
        self.edad = edad
        self.tamaño = tamaño
        self.peso = peso
        self.altura = altura
        self.fecha = fecha
        self.genero = genero
        self.tipo_de_alimento = tipo_de_alimento
        self.horarios_de_comida = horarios_de_comida
        self.vacunas = vacunas
        self.enfermedades = enfermedades

    def V_mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Peso: {self.peso}")
        print(f"Altura: {self.altura}")
        print(f"Fecha de ingreso: {self.fecha}")
        print(f"Género: {self.genero}")
        print(f"Tipo de alimento: {self.tipo_de_alimento}")
        print(f"Horarios de comida: {self.horarios_de_comida}")
        print(f"Vacunas: {self.vacunas}")
        print(f"Enfermedades: {self.enfermedades}")
        print('')  
        print('-'*30)
        print('')

        
g_zoologico = [
    L_Animal("León", 5, "Grande", 190, 120, (2020, 5, 20), "Macho", "Carnívoro", "12:00 PM", ["Rabia", "Parvovirus"], "Dermatitis"),
    L_Animal("Elefante", 10, "Muy Grande", 5400, 300, (2018, 8, 15), "Hembra", "Herbívoro", "9:00 AM", "Tétanos", "Ninguna"),
    L_Animal("Tigre", 4, "Grande", 220, 110, (2021, 4, 10), "Hembra", "Carnívoro", "1:00 PM", "Rabia", "Parásitos intestinales"),
    L_Animal("Jirafa", 7, "Muy Grande", 800, 500, (2019, 6, 25), "Macho", "Herbívoro", "10:00 AM", "Clostridiosis", "Ninguna"),
    L_Animal("Zebra", 6, "Mediano", 350, 140, (2020, 2, 10), "Hembra", "Herbívoro", "11:30 AM", ["Influenza equina"], ["Gastroenteritis"]),
    L_Animal("Cocodrilo", 12, "Grande", 500, 70, (2015, 7, 30), "Macho", "Carnívoro", "2:00 PM", "Todas", "Infección de piel"),
    L_Animal("Oso polar", 9, "Grande", 450, 130, (2017, 12, 1), "Hembra", "Carnívoro", "4:00 PM", ["Rabia", "Moquillo"], "Artritis"),
    L_Animal("Pingüino", 3, "Pequeño", 25, 45, (2021, 9, 20), "Macho", "Carnívoro", "8:00 AM", ["Salmonelosis"], []),
    L_Animal("Gorila", 15, "Grande", 160, 170, (2016, 4, 5), "Macho", "Omnívoro", "11:00 AM", "Tuberculosis", "Obesidad"),
    L_Animal("Canguro", 8, "Mediano", 85, 150, (2018, 11, 22), "Hembra", "Herbívoro", "5:00 PM", "Todas", "Luxación de cadera")
]

def vg_mostrar_anim_alimento(tipo_alimento):
    print(f"\nAnimales de tipo de alimento '{tipo_alimento}':")
    for animal in g_zoologico:
        if animal.tipo_de_alimento == tipo_alimento:
            animal.V_mostrar_info()


def menu():
    while True:
        print("\n--- Menú de Zoológico ---\n")
        print("1. Mostrar todos los animales")
        print("2. Clasificar por tipo de alimento: Carnívoro")
        print("3. Clasificar por tipo de alimento: Herbívoro")
        print("4. Clasificar por tipo de alimento: Omnívoro")
        print("5. Salir")
        L_opcion = input("\nSeleccione una opción: ")
        print('')
        print('-'*30)
        print('')
        
        if L_opcion == "1":
            for animal in g_zoologico:
                animal.V_mostrar_info()

        elif L_opcion == "2":
            vg_mostrar_anim_alimento("Carnívoro")

        elif L_opcion == "3":
            vg_mostrar_anim_alimento("Herbívoro")
            
        elif L_opcion == "4":
            vg_mostrar_anim_alimento("Omnívoro")

        elif L_opcion == "5":
            print("Saliendo del menú.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


menu()
