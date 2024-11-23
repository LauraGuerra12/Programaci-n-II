import csv

class Empresa():
    def __init__(self):
        self.valor=5000 #salario por hora
        self.admi={'bra':{'contraseña':'123'}}
        self.empleadosP=[]
        self.empleadosT=[]

        with open('C:/Users/Brayan David/Desktop/planta.csv', newline='') as fel:
            leer=csv.reader(fel, delimiter=';' )
            self.empleadosP=list(leer)
            
        with open('C:/Users/Brayan David/Desktop/temporal.csv', 'r', newline='') as fel:
            leer=csv.reader(fel, delimiter=';' )
            self.empleadosT=list(leer)

            

    def menu(self):
        bra1=int(input('''que accion deseas realizar
                            1. Agregar empleados
                            2. Calcular salarios
                            3. ver informacion de empleados
                            4. ver cuantos empleados ingresaron'''))

        if bra1==1:
            self.agre()
        elif bra1==2:
            self.calcular()
        elif bra1==3:
            bra4=int(input('''deseas ver informacion de:
                                    1. empleados de planta
                                    2. empleados temporales'''))
            if bra4==1:
                self.verP()
            elif bra4==2:
                self.verT()
            else:
                print('informacion invalida')
                self.menu()
                
        elif bra1==4:
            self.verTotalP()
                
        else:
            print('informacion invalida')
            self.menu()
        

    def agre(self):
        self.bra2=int(input('''deseas agregar
                                    1. empleados de planta
                                    2. empleados temporales '''))
        if self.bra2==1:
            self.info_P()
        elif self.bra2==2:
            self.info_T()
        else:
            print('informacion incvalida')
            self.agre()
            

    def info_P(self):
        ñ=int(input('cuantos empleados deseas ingresar'))
        self.contador=0
        for i in range(ñ):
            self.nombre=input('agregue el nombre del empleado\n')
            self.apellido=input('agregue el apellido del empleado\n')
            self.documento=input('agregue el documento del empleado\n')
            self.horas=int(input('agregue las horas trabajadas'))
            self.salario=(self.horas*5000)
            self.contador=self.contador+1
            self.empleadosP.append([self.nombre, self.apellido, self.documento, self.salario, self.contador])
        self.escribir_P()

    def escribir_P(self):
        with open('C:/Users/Brayan David/Desktop/planta.csv', 'a', newline='') as po:
            escri=csv.writer(po, delimiter=';')
            escri.writerows(self.empleadosP)
        print('se ha registrado exitosamente')
        self.menu()

    def info_T(self):
        l=int(input('cuantos empleados deseas ingresar'))
        self.contador1=0
        for i in range(l):
            self.nombre1=input('agregue el nombre del empleado\n')
            self.apellido1=input('agregue el apellido del empleado\n')
            self.documento1=input('agregue el documento del empleado\n')
            self.horas1=int(input('agregue las horas trabajadas'))
            self.salario1=(self.horas1*5000)
            self.contador1=self.contador1+1
            self.empleadosT.append([self.nombre1, self.apellido1, self.documento1, self.salario1, self.contador1])
        self.escribir_T()

    def escribir_T(self):
        with open('C:/Users/Brayan David/Desktop/temporal.csv', 'a', newline='') as po:
            escri=csv.writer(po, delimiter=';')
            escri.writerows(self.empleadosT)
        print('se ha registrado exitosamente')
        self.menu()

    def calcular(self):
        self.bra3=int(input('ingrese las horas que se ha trabajado'))
        self.salarioo=(5000*self.bra3)
        print(self.salarioo)
        self.menu()

    def verP(self):
        with open('C:/Users/Brayan David/Desktop/planta.csv', 'r', newline='') as fel:
            leer=csv.reader(fel, delimiter=';' )
            self.empleadosP=list(leer)
        for i in self.empleadosP:
            print(i)
        self.menu()

    def verT(self):
        with open('C:/Users/Brayan David/Desktop/temporal.csv', 'r', newline='') as fel:
            leer=csv.reader(fel, delimiter=';' )
            self.empleadosT=list(leer)
        for i in self.empleadosT:
            print(i)
        self.menu()

    def verTotalP(self):
        total_empleados = len(self.empleadosP)
        print('El total de empleados de planta es:', total_empleados)
        self.menu()



        

a=Empresa()
a.menu()

    
        

    
        
        
