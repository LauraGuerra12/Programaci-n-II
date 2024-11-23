##class Alumno:
##    def inicializar(self,nombre,nota):
##        self.nombre=nombre
##        self.nota=nota
##    def imprimir(self):
##        print("Nombre: ",self.nombre)
##        print("Nota: ",self.nota) 
## 
##    def resultado(self):
##        if self.nota < 5:
##            print("El alumno ha suspendido")
##        else: 
##            print("El alumno ha aprobado") 
## 
##alumno1=Alumno()
##alumno2=Alumno() 
##alumno1.inicializar("ivan",8)
##alumno2.inicializar("juan",4) 
##alumno1.imprimir()
##alumno1.resultado()
##alumno2.imprimir()
##alumno2.resultado() 
##
##
##
##
##
##class Triangulo:
##    def inicializar(self):
##        self.lado1=int(input("Ingrese el valor del primer lado: "))
##        self.lado2=int(input("Ingrese el valor del segundo lado: "))
##        self.lado3=int(input("Ingrese el valor del tercer lado: "))
##        
##    def imprimir(self):
##        print("Los lados del triángulo tienen el valor de") 
## 	print("Lado 1: ",self.lado1)
## 	print("Lado 2: ",self.lado2)
## 	print("Lado 3: ",self.lado3)
##
##    def mayor(self):
##        print("El lado mayor es")
##        if self.lado1>self.lado2 and self.lado1>self.lado3:
##            print("Lado 1: ",self.lado1)
##        elif self.lado2>self.lado3:
##            print("Lado 2: ",self.lado2)
##        else:
##            print("Lado 3: ",self.lado3)
##
##    def tipo(self):
##        if self.lado1==self.lado2 and self.lado1==self.lado3:
##            print("Es un triángulo equilátero")
##        elif self.lado1!=self.lado2 and self.lado1!=self.lado3:
##            print("Es un triángulo escaleno")
##        else: 
## 	    print("Es un triángulo isósceles")
## 	    figura=Triangulo() figura.inicializar() figura.imprimir() figura.mayor() figura.tipo()
##

###Código usando el constructor: 
##class Calculadora:
##    def __init__(self):
##        self.valor1=int(input("Ingrese el primer valor: "))
##        self.valor2=int(input("Ingrese el segundo valor: "))
##        self.menu()
##    def suma(self):
##        suma=self.valor1+self.valor2
##        print("El resultado de la suma de los valores es: ",suma)
##    def resta(self):
##        resta=self.valor1-self.valor2
##        print("El resultado de la resta de los valores es: ",resta)
##    def producto(self):
##        pro=self.valor1*self.valor2
##        print("El resultado de la multiplicación de los valores es: ",pro)
##    def division(self):
##        div=self.valor1/self.valor2
##        print("El resultado de la división de los valores es: ",div)
##    def imprimir(self):
##        print("Los valores son: ")
##        print("Valor 1: ",self.valor1)
##        print("Valor 2: ",self.valor2)
##    def menu(self):
##        opcion = input('ingrese 1: suma, 2: resta, 3: producto, 4: division, 5: mostrar, 6: Salir')
##        if opcion == '1':
##            self.suma()
##        elif opcion == '2':
##            self.resta()
##        elif opcion == '3':
##            self.producto()
##        elif opcion == '4':
##            self.division() 
##        elif opcion == '5':
##            self.imprimir()
##        elif opcion == '6':
##            exit()    
##        else:
##            print('error de ingreso')
##            self.menu()        
##
##while True:
##    calcular=Calculadora()


##calcular.imprimir()
##calcular.suma()
##calcular.resta()
##calcular.multiplicacion()
##calcular.division()


##class Persona():
##    nombre = None #'Hector'
##    apellido = 'Franco'
##    trabajo = 'docente'
##
##    def mostrar(self):
##        print(f"Su nombre es {self.nombre}, con apellido {self.apellido} y su trabajo es {self.trabajo}")
##
##    def si(self):
##        print('Somos lo mejor de la UIS')
        


##Ejercicio de clase: 
##Realizar un programa que conste de una clase llamada Alumno
##que tenga como atributos el nombre, apellidos, código y la nota del alumno.
##Definir los métodos para inicializar sus atributos, imprimirlos y 
##mostrar un mensaje con el resultado de la nota y si ha aprobado o no
class Alumno():

    def __init__(self): #usando el metodo constructor
        self.nombre=input('nombre')
        self.apellido=input('apellido')
        self.codigo=int(input('codigo'))
        self.nota=int(input('nota'))
        
##    def inicializar(self): #ese es una forma de pedir los datos
##        self.nombre=input('nombre')
##        self.apellido=input('apellido')
##        self.codigo=int(input('codigo'))
##        self.nota=int(input('nota'))

    def resultado(self):
        if self.nota<5:
            print(f"El alumno {self.nombre} {self.apellido} con codigo {self.codigo} ha perdido")
        else:
            print(f"El alumno {self.nombre} {self.apellido} con codigo {self.codigo} ha aprobado")

alumno1=Alumno()
alumno2=Alumno()
#alumno1.inicializar("ivan","guerra",2024,8)
#alumno1.inicializar()
alumno1.resultado()

