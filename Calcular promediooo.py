
def menu():
    bra1=int(input(''' bienvenido a la calculadora de promedios si quieres dar inicio marca
                        1 hacer promedio con creditos
                        2 hacer promedio sin creditos\n'''))
    if bra1==1:
        bra2()
    if bra1==2:
        bra10()
    else:
        print('informacion no valida')

def bra2():
    bra3=int(input('ingrese el numero de materias\n'))
    bra7=0
    bra9=0
# Brayan David Castañeda Zarate cod:2225188
    for i in range(bra3):
        bra4=input('ingrese la materia\n')
        bra5=float(input('ingrese la nota\n'))
        bra6=int(input('ingrese los creditos que tiene esa materia\n'))
        bra9=bra9+bra6
        bra8=(bra5*bra6)
        bra7=(bra7+bra8)
    bra7=bra7/bra9
    print('el promedio es ', bra7)

def bra10():
    bra11=int(input('ingrese el numero de materias\n'))
    bra12=0
    bra13=0
    for i in range(bra11):
        bra14=input('ingrese la materia\n')
        bra15=float(input('ingrese la nota\n'))
        bra12=bra12+bra15
    print('el promedio es ', bra12/bra11)



menu()
