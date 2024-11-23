#EJEMPLOS DE ENCAPSULAMIENTO: 
# ENCAPSULAMIENTO: Ocultamiento de datos del estado interno
#para proteger la integridad del objeto.
#atributos públicos (se pueden ver) y privados(no se pueden ver facilmente)

#ejercicio 1 de encapsulamiento
##
##class Cliente():
##    def _init_(self):
##        self.nombre=input('nombre')
##        self.tipocuenta=input('tipo de cuenta')
##        self.__codigo=1234 #encapsula el dato
##
##    def __cuenta(self):
##        print('cuenta de procesamiento')
##           
##    def getcodigo(self):  #con este método busca el código encapsulado
##        return self.__codigo
##
##
##cli=Cliente()
##print(cli.Cliente_codigo) #puede ver el código guardado ->1234
##cli.Cliente_cuenta()#->cuenta de procesamiento



#ejercicio 2 de encapsulamiento

##class Persona():
##
##    def _init_ (self, codigo, nombre, edad):
##        self.__codigo= codigo 
##        self.__nombre= nombre   
##        self.edad= edad
##
##
##    def saludar (self):
##        print ('hola' , self.nombre)
##

#ejercicio 3 de encapsulamiento
class Banco():
    def __init__(self):
        self.nombre = input('ingrese su nombre y apellidos: ')
        self.direccion = input('ingrese su dirección: ')
        self.telefono = int(input('ingrese su numero telefonico: '))
        self.tipocuenta = input('ingrese tipo de cuenta: ')
        self.apertura = float(input('Cuanto dinero abre la cuenta'))
        self.__dinero = self.apertura - 50000.0 #float(input('ingrese dinero de apertura cuenta: '))

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



     









        
#comentarios
###podemos acceder a un atributo privado asi:
###nombreobjeto._nombreclase__nombreatributo
##ejemplo: a.Banco_dinero     

###creación de objetos para probar el programa
##p1=Persona(1,'julian',12)
##p2=Persona(122222,'hector', 15)
##print (p1.Persona_codigo)
##print (p1.Persona_nombre)
##print (p1.edad)
##
##print (p2.Persona_codigo)
##print (p2.Persona_nombre)
##print (p2.edad)
##
##p1.nombre = 'hector julian'
##p1.saludar()
