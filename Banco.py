#ejercicio 3 de encapsulamiento
import pandas as pd
class Banco():
    def __init__(self):
        self.nombre = input('ingrese su nombre y apellidos: ')
        self.direccion = input('ingrese su dirección: ')
        self.telefono = int(input('ingrese su numero telefonico: '))
        self.tipocuenta = input('ingrese tipo de cuenta: ')
        self.apertura = float(input('Cuanto dinero abre la cuenta'))
        self.__dinero = self.apertura - 50000.0 #float(input('ingrese dinero de apertura cuenta: '))

    


    def Agregar(self):
        nombre = input("Ingresa su nombre: ")
        password = input("Ingresa su contraseña: ")
        direccion = input("Ingrese su direccion: ")
        correo = input("Ingrese su correo electrónico: ")
        telefono = int(input('Ingrese su telefono: '))
        tipo_cuenta = int(input('Ingrese su tipo de cuenta: '))

        # Crear un DataFrame con la nueva fila
        nuevo_dato = pd.DataFrame({'Nombre': [nombre], 'Contraseña': [password],'Direccion': [direccion], 'Correo': [self.correo], 'Telefono': [self.telefono], 'Tipo de Cuenta': [tipo_cuenta]})
        # Agregar la nueva fila al DataFrame existente
        self.df = pd.concat([self.df, nuevo_dato], ignore_index=True)
        # Guardar los cambios en el archivo CSV
        self.df.to_csv(self.archivo_csv, index=False)

        print(f"Datos guardados correctamente en {self.archivo_csv}")
        print(self.df)

    def Verificar(self):
        nombre = input("Ingresa su nombre: ")
        password = input("Ingresa su contraseña: ")
        if nombre in self.df['Nombre'].values and password in self.df['Contraseña'].values:
            self.Menu()
        else:
            self.Agregar()


    def Recibo(self):
        print(self.nombre, self.direccion, self.telefono, self.tipocuenta, self.__dinero)
        return (self.nombre, self.direccion, self.telefono, self.tipocuenta, self.__dinero)

    def Retirar(self, valor):
        self.__dinero-=valor

    def Consignar(self, valor):
        self.__dinero+=valor

    def Menu(self):
        print('Bienvenido al Banco....')
        op = input('''Ingrese la opcion que desea:
                        1. Ver Recibo
                        2. Retitar
                        3. Consignar\n''')
        if op == "1":
            self.Recibo()
        elif op == "2":     #Pilas con el parametro del metodo
            value = float(input("Cuanto desea retirar: "))
            self.Retirar(value)
        elif op == "3":     #Pilas con el parametro del metodo
            self.Consignar()
        else:
            print("Error de ingreso")