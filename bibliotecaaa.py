import csv
import datetime

class Biblioteca():
    def __init__(self):
        self.usuarioos={}
        self.admi={"bra":{"contraseña": "123"}}
        self.libros={}

    
        

    def menu(self):
        a=int(input('''Bienvenidos a la bibliote de la U
                            desea ingresar como
                                1 administrador
                                2 usuario: '''))
        if a==1:
            self.administrador()
        if a==2:
            self.usuario()

    def administrador(self):
        self.name=input("por favor ingrese su nombre de usuario\n")
        if self.name in self.admi:
            self.passw=input("ingrese su contraseña\n")
            if self.passw == self.admi[self.name]["contraseña"]:
                self.opciones()

        else:
            print('error')
            self.administrador()

    def opciones(self):

        b=int(input('''has ingreasado como administrador marca la opcion a realizar
                1. Crear libros
                2. Crear usuarios
                3. Modificar
                4. menu\n'''))
        if b==1:
            self.crearL()
        elif b==2:
            self.crearU()

        elif b==3:
            self.modificar()

        elif b==4:
            self.menu()

        else:
            print('informacion invalida')
            self.opciones()
            
    def crearL(self):
        self.nombre=input('ingrese el nombre del libro: ')
        self.inventario=input('ingrese el numero de inventario: ')
        self.autor=input('ingrese el nombre del autor: ')
        self.tema=input('ingrese el tema del libro: ')
        self.Npaginas=input('ingrese el numero de paginas: ')
        self.Cejemplares=input('ingrese la cantidad de ejemplares: ')
        self.precio=input('ingrese el precio de cada libro: ')
        self.libros[self.nombre]={'inventario':self.inventario, 'autor':self.autor, 'tema':self.tema, 'Npaginas':self.Npaginas, 'Cejemplares':self.Cejemplares, 'precio':self.precio }
        print('se ha ingresado correctamente')
        self.opciones()
        
    def crearU(self):
        self.id=input('ingrese el usuario que va a registrar')
        self.contra=input('ingrese la contraseña para el usuario')
        self.usuarioos[self.id]={'contraseña':self.contra}
        print('el usuario se ha registrado exitosamente')
        self.opciones()

    def modificar(self):
        q=int(input('''Marca la opcion de lo que deseas modificar:
                        1. Nombre del libro
                        2. Numero de inventario
                        3. Nombre del autor
                        4. Numero de paginas
                        5. Cantidad de ejemplares
                        6. El precio
                        7. volver a menu\n'''))
        if q==1:
            self.nombre2=input('ingrese el nuevo nombre')
            self.libros[self.nombre3] = self.contacto.pop(self.nombre)
            print('Nombre actualizado correctamente.')
            self.modificar()
        if q==2:
            self.nombre2=input('ingrese el nombre del libro que deseas modificar: ')
            self.inve_N=input('ingrese el nuevo numero de invemtario: ')
            self.libros[self.nombre2]['inventario']=self.inve_N
            print('se ha modificado exitosamente')
            self.modificar()
        if q==3:
            self.nombre2=input('ingrese el nombre del libro que deseas modificar: ')
            self.autor_N=input('ingrese el nuevo numero de invemtario: ')
            self.libros[self.nombre2]['autor']=self.autor_N
            print('se ha modificado exitosamente')
            self.modificar()
        if q==4:
            self.nombre2=input('ingrese el nombre del libro que deseas modificar: ')
            self.paginas_N=input('ingrese el numero de paginas: ')
            self.libros[self.nombre2]['Npaginas']=self.paginas_N
            print('se ha modificado exitosamente')
            self.modificar()
        if q==5:
            self.nombre2=input('ingrese el nombre del libro que deseas modificar: ')
            self.cantida_E=input('ingrese la cantidad de ejemplares: ')
            self.libros[self.nombre2]['Cejemplares']=self.cantida_E
            print('se ha modificado exitosamente')
            self.modificar()
        if q==6:
            self.nombre2=input('ingrese el nombre del libro que deseas modificar: ')
            self.precio_N=input('ingrese la cantidad de ejemplares: ')
            self.libros[self.nombre2]['Cejemplares']=self.precio_N
            print('se ha modificado exitosamente')
            self.modificar()

        if q==7:
            self.menu()

    def usuario(self):
        self.r=input('ingrese el usuario: ')
        if self.r in self.usuarioos:
            self.contrase=input('ingrese la contra: ')
            if self.contrase==self.usuarioos[self.r]['contraseña']:
                self.reservar()
            else:
                print('contraseña incorrecta')
                self.usuario()
        else:
            print('usuario incorrecto')
            self.usuario()

            
            
                
    def reservar(self):
        p=int(input('''que opcion deseas realizar
                        1. ver libros disponibles
                        2. reservar un libro
                        3. sacar prestamo
                        4. devolucion del libro
                        5. volver a menu\n'''))
        if p==1:
            self.verL()
        elif p==2:
            self.reservacion()
        elif p==3:
            self.prestamo()
        elif p==4:
            self.devolucion()
        elif p==5:
            self.menu()
        else:
            print('informacion invalida')
            self.reservar()

    def verL(self):
        for libro in self.libros:
            print("Nombre: ", libro)
            print("Inventario: ", self.libros[libro]["inventario"])
            print("Autor: ", self.libros[libro]["autor"])
            print("Tema: ", self.libros[libro]["tema"])
            print("Páginas: ", self.libros[libro]["Npaginas"])
            print("Ejemplares: ", self.libros[libro]["Cejemplares"])
            print("Precio: ", self.libros[libro]["precio"])
        self.reservar()

    def reservacion(self):
        nombre_libro=input('ingrese el nombre del libro que deseas reservar: ')
        if nombre_libro in self.libros:
            if int(self.libros[nombre_libro]["Cejemplares"]) > 0:
                self.libros[nombre_libro]["Cejemplares"] = int(self.libros[nombre_libro]["Cejemplares"]) - 1
                print("Libro reservado exitosamente.")
            else:
                print('el libro no se encuentra disponibe')
        else:
            print('libro no encontrado')
        self.reservar()

    def prestamo(self):
        nombre_libro = input("Ingrese el nombre del libro que desea sacar en préstamo: ")
        if nombre_libro in self.libros:
            if int(self.libros[nombre_libro]["Cejemplares"]) > 0:
                self.libros[nombre_libro]["Cejemplares"] = int(self.libros[nombre_libro]["Cejemplares"]) - 1
                fecha_actual = datetime.date.today()
                print(f"Préstamo realizado exitosamente. Fecha de préstamo: {fecha_actual}")
            else:
                print("No hay ejemplares disponibles.")
        self.reservar()

    def devolucion(self):
        nombre_libro = input('Ingrese el nombre del libro que desea devolver: ')
        if nombre_libro in self.libros:
            self.libros[nombre_libro]["Cejemplares"] = int(self.libros[nombre_libro]["Cejemplares"]) + 1
            fecha_devolucion = datetime.date.today()
            fecha_prestamo = input('Ingrese la fecha en que se realizó el préstamo (YYYY-MM-DD): ')
            fecha_prestamo = datetime.datetime.strptime(fecha_prestamo, '%Y-%m-%d').date()
            dias_prestamo = (fecha_devolucion - fecha_prestamo).days
            if dias_prestamo > 7:
                multa = (dias_prestamo - 7) * 10  # Suponiendo una multa de $10 por día de retraso
                print(f"Libro devuelto. Se ha generado una multa de ${multa} por devolución tardía.")
            else:
                print("Libro devuelto. Sin cargos adicionales.")
        else:
            print('Libro no encontrado en la biblioteca.')
        self.reservar()
        
        
    
a=Biblioteca()
a.menu()

        
        
        
