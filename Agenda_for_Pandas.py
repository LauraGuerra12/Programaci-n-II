import pandas as pd

class Agenda():
    def __init__(self):
        self.contactos = pd.DataFrame(columns=['nombre', 'telefono', 'correo'])

    def Anadir(self):
        print('-' * 20)
        print(' ')
        print('Añadir Nuevo Contacto')
        print(' ')
        nombre = input('Nombre del contacto: ')
        telefono = input('Teléfono del contacto: ')
        correo = input('Correo del contacto: ')
        nuevo_contacto = pd.DataFrame({'nombre': [nombre], 'telefono': [telefono], 'correo': [correo]})
        self.contactos = pd.concat([self.contactos, nuevo_contacto], ignore_index=True)
        print('Contacto añadido correctamente')
        self.menu()

    def Lista_contactos(self):
        print('-' * 20)
        print(' ')
        print('Lista de Contactos')
        print(' ')
        if self.contactos.empty:
            print('La agenda está vacía.')
        else:
            print(self.contactos)
        self.menu()

    def Buscar_contacto(self):
        print('-' * 20)
        print(' ')
        print('Buscar Contacto')
        print(' ')
        nombre = input('Ingrese el nombre del contacto que desea buscar: ')
        contacto = self.contactos[self.contactos['nombre'].str.lower() == nombre.lower()]
        if not contacto.empty:
            print(contacto)
        else:
            print("Contacto no encontrado.")
        self.menu()

    def Editar_contacto(self):
        print('-' * 20)
        print(' ')
        print('Editar Contacto')
        print(' ')
        nombre = input('Ingrese el nombre del contacto que quiere editar: ')
        contacto_idx = self.contactos[self.contactos['nombre'].str.lower() == nombre.lower()].index
        if not contacto_idx.empty:
            idx = contacto_idx[0]
            new_nombre = input(f'Nuevo nombre (presione Enter para dejar {self.contactos.at[idx, "nombre"]}): ') or self.contactos.at[idx, 'nombre']
            new_telefono = input(f'Nuevo teléfono (presione Enter para dejar {self.contactos.at[idx, "telefono"]}): ') or self.contactos.at[idx, 'telefono']
            new_correo = input(f'Nuevo correo (presione Enter para dejar {self.contactos.at[idx, "correo"]}): ') or self.contactos.at[idx, 'correo']
            self.contactos.at[idx, 'nombre'] = new_nombre
            self.contactos.at[idx, 'telefono'] = new_telefono
            self.contactos.at[idx, 'correo'] = new_correo
            print('Contacto editado y guardado correctamente.')
        else:
            print("Contacto no encontrado.")
        self.menu()

    def Eliminar_contacto(self):
        print('-' * 20)
        print(' ')
        print('Eliminar Contacto')
        print(' ')
        nombre = input('Ingrese el nombre del contacto que quiere eliminar: ')
        contacto_idx = self.contactos[self.contactos['nombre'].str.lower() == nombre.lower()].index
        if not contacto_idx.empty:
            self.contactos = self.contactos.drop(contacto_idx)
            print(f'Contacto {nombre} eliminado correctamente.')
        else:
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
agenda.menu()
