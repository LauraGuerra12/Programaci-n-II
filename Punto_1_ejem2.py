'''Diseñe un programa aplicando POO que nos sirva como agenda de contactos, tenga en cuenta todos los datos necesarios para un objeto.'''


class Contacto:
    def __init__(self, nombre, telefono, email, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.direccion = direccion

    def mostrar_informacion(self):
        return (f"Nombre: {self.nombre}\n"
                f"Teléfono: {self.telefono}\n"
                f"Email: {self.email}\n"
                f"Dirección: {self.direccion}")

    def editar_telefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono

    def editar_email(self, nuevo_email):
        self.email = nuevo_email

    def editar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion


class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)
        print(f"Contacto '{contacto.nombre}' agregado a la agenda.")

    def mostrar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            for contacto in self.contactos:
                print(contacto.mostrar_informacion())
                print("-" * 30)

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                return contacto
        return None

    def eliminar_contacto(self, nombre):
        contacto = self.buscar_contacto(nombre)
        if contacto:
            self.contactos.remove(contacto)
            print(f"Contacto '{nombre}' eliminado de la agenda.")
        else:
            print(f"Contacto '{nombre}' no encontrado.")

    def editar_contacto(self, nombre):
        contacto = self.buscar_contacto(nombre)
        if contacto:
            print("Seleccione el dato que desea actualizar:")
            print("1. Teléfono")
            print("2. Email")
            print("3. Dirección")
            opcion = input("Ingrese el número de opción: ")

            if opcion == '1':
                nuevo_telefono = input("Ingrese el nuevo teléfono: ")
                contacto.editar_telefono(nuevo_telefono)
            elif opcion == '2':
                nuevo_email = input("Ingrese el nuevo email: ")
                contacto.editar_email(nuevo_email)
            elif opcion == '3':
                nueva_direccion = input("Ingrese la nueva dirección: ")
                contacto.editar_direccion(nueva_direccion)
            else:
                print("Opción no válida.")
        else:
            print(f"Contacto '{nombre}' no encontrado.")


def main():
    agenda = Agenda()
    
    while True:
        print("\n--- Agenda de Contactos ---\n")
        print("1. Agregar Contacto")
        print("2. Mostrar Contactos")
        print("3. Buscar Contacto")
        print("4. Editar Contacto")
        print("5. Eliminar Contacto")
        print("6. Salir")
        opcion = input("\nSeleccione una opción: ")
        print('')
        print('-' * 30)
        print('')

        if opcion == '1':
            nombre = input("Nombre del contacto: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            direccion = input("Dirección: ")
            contacto = Contacto(nombre, telefono, email, direccion)
            agenda.agregar_contacto(contacto)

        elif opcion == '2':
            agenda.mostrar_contactos()

        elif opcion == '3':
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            contacto = agenda.buscar_contacto(nombre)
            if contacto:
                print("\nInformación del contacto:")
                print(contacto.mostrar_informacion())
            else:
                print(f"Contacto '{nombre}' no encontrado.")

        elif opcion == '4':
            nombre = input("Ingrese el nombre del contacto a editar: ")
            agenda.editar_contacto(nombre)

        elif opcion == '5':
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            agenda.eliminar_contacto(nombre)

        elif opcion == '6':
            print("Saliendo de la agenda...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
