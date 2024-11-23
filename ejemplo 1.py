class Agenda():
    def __init__(self):
        self.contactos = []

    def Anadir(self):
        print('-' * 20)
        print(' ')
        print('Añadir Nuevo Contacto')
        print(' ')
        nombre = input('Nombre del contacto: ')
        telefono = input('Teléfono del contacto: ')
        correo = input('Correo del contacto: ')
        self.contactos.append({'nombre': nombre, 'telefono': telefono, 'correo': correo})
        print('Contacto añadido correctamente')
        self.menu()

    def Lista_contactos(self):
        print('-' * 20)
        print(' ')
        print('Lista de Contactos')
        print(' ')
        if not self.contactos:
            print('La agenda está vacía.')
        else:
            for i, contacto in enumerate(self.contactos, 1):
                print(f'{i}. Nombre: {contacto["nombre"]}, Teléfono: {contacto["telefono"]}, Correo: {contacto["correo"]}')
        self.menu()
        

    def Buscar_contacto(self):
        print('-' * 20)
        print(' ')
        print('Buscar Contacto')
        print(' ')
        nombre = input('Ingrese el nombre del contacto que desea buscar: ')
        for contacto in self.contactos:
            if contacto['nombre'].lower() == nombre.lower():
                print(f'Nombre: {contacto["nombre"]}, Teléfono: {contacto["telefono"]}, Correo: {contacto["correo"]}')
                self.menu()
                return
        print("Contacto no encontrado.")
        self.menu()

        
    def Editar_contacto(self):
        print('-' * 20)
        print(' ')
        print('Editar Contacto')
        print(' ')
        nombre = input('Ingrese el nombre del contacto que quiere editar: ')
        for contacto in self.contactos:
            if contacto['nombre'].lower() == nombre.lower():
                new_nombre = input(f'Nuevo nombre (presione Enter para dejar {contacto["nombre"]}): ') or contacto['nombre']
                new_telefono = input(f'Nuevo teléfono (presione Enter para dejar {contacto["telefono"]}): ') or contacto['telefono']
                new_correo = input(f'Nuevo correo (presione Enter para dejar {contacto["correo"]}): ') or contacto['correo']
                contacto['nombre'] = new_nombre
                contacto['telefono'] = new_telefono
                contacto['correo'] = new_correo
                print('Contacto editado y guardado correctamente.')
                self.menu()
                return
        print("Contacto no encontrado.")
        self.menu()


    def Eliminar_contacto(self):
        print('-' * 20)
        print(' ')
        print('Eliminar Contacto')
        print(' ')
        nombre = input('Ingrese el nombre del contacto que quiere eliminar: ')
        for contacto in self.contactos:
            if contacto['nombre'].lower() == nombre.lower():
                self.contactos.remove(contacto)
                print(f'Contacto {nombre} eliminado correctamente.')
                self.menu()
                return
        print("Contacto no encontrado.")
        self.menu()
        

    def menu(self):
        print('\n Menú ')
        print('1. Añadir contacto')
        print('2. Lista de contactos')
        print('3. Buscar contacto')
        print('4. Editar contacto')
        print('5. Eliminar contacto')
        print('6. Salir')

        opcion = int(input('Seleccione una opción: '))

        if opcion == 1:
            self.Anadir()
        elif opcion == 2:
            self.Lista_contactos()
        elif opcion == 3:
            self.Buscar_contacto()
        elif opcion == 4:
            self.Editar_contacto()
        elif opcion == 5:
            self.Eliminar_contacto()
        elif opcion == 6:
            print('Cerrando la agenda.')
            exit()
        else:
            print('Opción no válida. Inténtalo de nuevo.')
            self.menu()

agenda = Agenda()
a=agenda.menu()