import csv

class Cine:
    def __init__(self):
        self.comidabra={}
        self.peliculas={'kung fun panda':{'hora':'2 PM'},'cars':{'hora':'4 PM'}, 'los increibles':{'hora':'6 PM'}}
        self.entradas=[]
        self.foot=[]
        self.suma=0
        
        with open('C:/Users/Brayan David/Desktop/comidas.csv', 'r', newline='') as fel:
            reader=csv.reader(fel, delimiter=';')
            next(reader)
            for row in reader:
                self.comidabra[row[0]] = {'precio': row[1]}
    
        with open('C:/Users/Brayan David/Desktop/peliculas.csv', 'r', newline='') as fel:
            reader=csv.reader(fel, delimiter=';')
            next(reader)
            for row in reader:
                self.peliculas[row[0]] = {'hora': row[1]}

        with open('C:/Users/Brayan David/Desktop/entradas.csv', 'r', newline='') as fel:
            leer=csv.reader(fel, delimiter=';' )
            entradas=list(leer)

        self.empleados={'bra':{'contraseña':'123'}}

        self.usuarios={}
        
    def menu(self):
        a=int(input('''de que manera deseas ingresar
                        1. Cliente
                        2. empleado'''))
        if a==1:
            self.clientes_n()
        elif a==2:
            self.ingreso()
        else:
            print('informacion invalida')
            self.menu()
    
    def ingreso(self):
        self.d=input('ingrese el usuario')
        if self.d in self.empleados:
            self.contra=input('ingrese la contraseña')
            if self.contra==self.empleados[self.d]['contraseña']:
                self.modificacion()
        else:
            print('informacion invalida')
            self.ingreso()
                
    def modificacion(self):        
        e=int(input('''que deseas modificar
                        1. comidas
                        2. agregar a clientes frecuentes
                        3. peliculas
                        4. volver a menu'''))
        if e==1:
            self.comidaa()
        elif e==2:
            self.clientes()
        elif e==3:
            self.peliculaas()
        elif e==4:
            self.menu()
        else:
            print('informacion invalida')
            self.modificacion()

    def comidaa(self):
        g='si'
        f=int(input('''que deseas modificar
                1. agregar comida
                2. modificar precio
                3. eliminar
                4. volver a menu'''))
        if f==1:
            while g=='si':
                self.comid=input('que comida deseas ingresar\n')
                self.preci=input('que precio deseas ingresar\n')
                self.comidabra[self.comid]={'precio':self.preci}
                print(f'la comida {self.comid} ha sido registrado exitosamente.\n')
                self.foot.append([self.comid, self.preci])
                g=input('marca "si" si deseas ingresar otro alimento')
                
            self.escribir_com()
                
        elif f==2:
            while g=='si':
                self.comidd=input('ingresa la comida que deseas modificar')
                if self.comidd in self.comidabra:
                    self.prec=input('ingresa el precio nuevo')
                    self.comidabra[self.comidd]['precio']=self.prec
                g=input('digite "si" si deseas modificar otro alimento')
    
                
        elif f==3:
            while g=='si':
                self.comiddd=input('que alimento desea eliminar')
                if self.comiddd in self.comidabra:
                    self.comidabra.pop(self.comiddd)
                g=input('si deseas eliminar otro alimento marque "si"')
            self.escribir_com2()

        elif f==4:
            self.menu()

        else:
            print('informacion invalida')
            self.comidaa()

                    
    def escribir_com(self):
        with open('C:/Users/Brayan David/Desktop/comidas.csv', 'w', newline='') as pol:
            escrib=csv.writer(pol, delimiter=';')
            escrib.writerow(['comid', 'precio']) 
            for comid, info in self.comidabra.items():
                escrib.writerow([comid, info['precio']])
        print('Ha agregado la comida correctamente')
        self.comidaa() 
    

    
                 

    def escribir_com2(self):

        with open('C:/Users/Brayan David/Desktop/comidas.csv', 'w', newline='') as pol:
            escrib=csv.writer(pol, delimiter=';')
            escrib.writerow(['comid', 'precio']) 
            for comid, info in self.comidabra.items():
                escrib.writerow([comid, info['precio']])
        print('Ha elimina la comida correctamente')
        self.comidaa() 
    

    def clientes(self):
        j='si'
        while j=='si':
            self.name=input('ingresa el nombre que deseas ingresar a clientes frecuentes')
            self.passw=input('ingrese la contraseña')
            self.usuarios[self.name]={'contraseña':self.passw}
            j=input('deseas ingresar un nuevo nuevo cliente')
            print('se ha registrado correctamente')

    def peliculaas(self):
        g='si'
        h=int(input('''que deseas modificar
                1. agregar pelicula
                2. modificar horario
                3. eliminar
                4. volver a menu'''))
        if h==1:
            while g=='si':
                self.peli=input('que pelicula deseas ingresar\n')
                self.horario=input('que horario deseas ingresar\n')
                self.peliculas[self.peli]={'hora':self.horario}
                print(f'la comida {self.peli} ha sido registrado exitosamente.\n')
                g=input('marca "si" si deseas ingresar otra pelicula')
                self.movie.append([self.peli , self.horario])
                self.escribir_peliculas()

        elif h==3:
            while g=='si':
                self.pelic=input('que alimento desea eliminar')
                if self.pelic in self.peliculas:
                    self.peliculas.pop(self.pelic)
                g=input('si deseas eliminar otro alimento marque "si"')
            self.escribir_peliculas3()

        elif h==4:
            self.menu()



    def escribir_peliculas(self):
        with open('C:/Users/Brayan David/Desktop/peliculas.csv', 'w', newline='') as pol:
            escrib=csv.writer(pol, delimiter=';')
            escrib.writerow(['peli', 'hora']) 
            for peli, info in self.peliculas.items():
                escrib.writerow([peli, info['hora']])
        print('Se ha agregado la pelicula correctamente')
        self.peliculaas()
        

    def escribir_peliculas3(self):
        with open('C:/Users/Brayan David/Desktop/peliculas.csv', 'w', newline='') as pol:
            escrib=csv.writer(pol, delimiter=';')
            escrib.writerow(['peli', 'hora']) 
            for peli, info in self.peliculas.items():
                escrib.writerow([peli, info['hora']])
        print('Se ha eliminado la pelicula correctamente')
        self.peliculaas()
        

    def clientes_C(self):
        j=input('''que opcion deseas elegir
                1. Clientes frecuentas
                2. clientes normales''')
        if j==1:
            self_clientes_f()
        if j==2:
            self_clientes_n()

    def clientes_n(self):
        k=input('''que accion deseas realizar
                1. ver cartelera
                2. comprar entrada
                3. ver comida
                4. ver entradas compradas''')
        if k=='1':
            for peli, i in self.peliculas.items():
                print(f'Pelicula: {peli}, hora: {i["hora"]}')
            self.clientes_n()
                

        if k=='2':
            self.tiquetes()


    def tiquetes(self):
        contador=0
        for peli, i in self.peliculas.items():
            print(f'Pelicula: {peli}, hora: {i["hora"]}\n')
            while self.suma<=10:
                ñ=input('que pelicula desea comprar: ')
                if ñ in self.peliculas:
                    k=int(input('cuantas entradas desea comprar: '))
                    for self.i in range(k):
                        i=contador+1
                        self.entradas.append([ñ,self.i])
                        self.escribir_tiquetes()
                self.suma=self.suma+self.i
        print('sala llena')
        self.clientes_n()
        


        
 

            
           

    def escribir_tiquetes(self):
        with open('C:/Users/Brayan David/Desktop/entradas.csv', 'a', newline='') as po:
            escri=csv.writer(po, delimiter=';')
            escri.writerows(self.entradas)
        print('se ha realizado la compra exitosamente')
        self.tiquetes()
        

        

a=Cine()
a.menu()
