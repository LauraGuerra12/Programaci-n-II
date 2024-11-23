usuarios = {"brayan": {"contraseña": "123"}, "lopez": {"contraseña": "456"}, "Julian": {"contraseña":"789"}, "Jhon":{"contraseña":"147"}, "Valeria":{"contraseña":"258"}}
Administrador = {"admi": {"contraseña":"1057"}}
nombres=set()
a="si"
b="si"
c="si"
d="si"
contador=0
contador1=0
contador2=0
admin=input("ingrese usuario del administrador\n")
if admin in Administrador:
    clav=input("ingrese clave del administrador\n")
    if clav==Administrador[admin]['contraseña']:
        a=input("desea abrir las votaciones\n")
        while a=="si":
            usuario=input('ingrese su usuario\n')
            if usuario in usuarios:
                password=input("por favor ingrese su contraseña\n")
                if password==usuarios[usuario]['contraseña']:
                    voto=int(input('''el usuario se encuentra registrado en la base de datos
                                    deseas votar por:
                                        1 Juan Carrascal
                                        2 Andres Medina
                                        3 Maria Cortez\n'''))
                    if voto==1:
                        contador=contador+1
                    elif voto==2:
                        contador1=contador1+1
                    elif voto==3:
                        contador2=contador2+1
                    else:
                        a=input('el voto es erroneo si quiere volverlo a intentar por favor marca "si"\n')

                else:
                    print("contraseña incorrecta")
            else:
                print('el usuario no aparece registrado\n')
            a=input('si otro usuario desea ingresar su voto o deseas volver a intentar marque "si"\n')
        print('''la votacion ha quedado de la siguiente manera
                                    juan carrascal=''',contador,'''votos
                                    Andres Medina=''',contador1,'''votos
                                    Maria Cortez=''',contador2,'''votos''')
    else:
        print("clave incorrecta")
        
else:
    d=input("error de ingreso del administrador si desea volverlo a intentar marque 'si'")
        

          
