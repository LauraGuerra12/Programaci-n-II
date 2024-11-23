#TKINTER + POO
#Realice una calculadora sencilla empleando los principales comandos de Tk con POO
from tkinter import *

class calculadora(Frame):#Frame=heredando de la clase Frame de tkinter, por eso se importa toda la libreria. 

    def __init__(self, master=None):
        super().__init__(master,width=320, height=170)
        self.master=master
        #PACK=es un tipo de posicionamiento para los widgets que ajusta todo los elementos acomodándolos entre sí,
        #para luego hacer la ventana raíz tan grande para contener todos estos elementos.
        self.pack()
        self.creaboton()

        
    def suma(self):
        a1=self.anum1.get()
        a2=self.anum2.get()
        r=float(a1)+float(a2)
        self.anum3.delete(0,'end')
        self.anum3.insert(0,r)

    def resta(self):
        a1=self.anum1.get()
        a2=self.anum2.get()
        r=float(a1)-float(a2)
        self.anum3.delete(0,'end')
        self.anum3.insert(0,r)

    def producto(self):
        a1=self.anum1.get()
        a2=self.anum2.get()
        r=float(a1)*float(a2)
        self.anum3.delete(0,'end')
        self.anum3.insert(0,r)

    def cociente(self):
        a1=self.anum1.get()
        a2=self.anum2.get()
        r=float(a1)/float(a2)
        self.anum3.delete(0,'end')
        self.anum3.insert(0,r)

    def creaboton(self):
        self.bnum1=Label(self, text='DATO 1')
        self.bnum1.config(fg='green', font=('Arial',16))#para configurar el texto.
        self.anum1=Entry(self)
        self.bnum2=Label(self, text='DATO 2')
        self.bnum2.config(fg='purple', font=('Arial',16))
        self.anum2=Entry(self)
        self.op=Button(self, text='suma', command=self.suma)
        self.op1=Button(self, text='resta', command=self.resta)
        self.op2=Button(self, text='Multiplicación', command=self.producto)
        self.op3=Button(self, text='División', command=self.cociente)
        self.bnum3=Label(self,text='Resultado')
        self.bnum3.config(fg='pink', font=('Arial',16))
        self.anum3=Entry(self)
        self.bnum1.place(x=10, y=10, width=100, height=30)
        self.anum1.place(x=120, y=10, width=100, height=30)
        self.bnum2.place(x=10, y=50, width=100, height=30)
        self.anum2.place(x=120, y=50, width=100, height=30)
        self.op.place(x=230,y=10, width=100, height=20)
        self.op1.place(x=230,y=40, width=100, height=20)
        self.op2.place(x=230,y=70, width=100, height=20)
        self.op3.place(x=230,y=100, width=100, height=20)
        self.bnum3.place(x=10, y=120, width=100, height=30)
        self.anum3.place(x=120, y=120, width=100, height=30)

vent=Tk()
vent.wm_title('Calculadora')
vent.geometry('400x200')
app=calculadora(vent)
app.mainloop()
