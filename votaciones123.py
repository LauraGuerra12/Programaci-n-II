estudiantes_registrados={'brayan':1057572282, 'santiago':123652, 'andres':253621}
usuarios = {}
registrados = set()

contador=0
contador1=0
contador2=0
a = "si"
b = "sii"
while a == "si":
    id_ = input("ingrese su nombre de usuario para registrar\n")
    contraseña = input("ingrese la contraseña para registrarse\n")
    if id_ not in usuarios:
        usuarios[id_] = {"contraseña": contraseña}
        print("el usuario ha sido registrado exitosamente.")
    else:
        print("el usuario ya está registrado.")
    a = input('si quiere agregar a otra persona por favor digite "si"\n')
    
while b == "sii":
    nombre = input("ingrese su usuario\n")
    if nombre in registrados:
        print("Este nombre ya se encuentra registrado en el sistema de votacion")
    elif nombre in usuarios:
        password = input("ingrese su contraseña\n")
        if password == usuarios[nombre]["contraseña"]:
            print('''Los estudiantes que se lanzaron a ser candidatos de personero son:
                            1. Andres Carrascal vota 01
                            2. Carlos Medina vota 02
                            3. Johan Cortez vota 03 ''')
            voto=int(input("ingrese su voto\n"))
            if voto==1 :
              contador=contador+1
            elif voto==2 :
              contador1=contador1+1
            elif voto==3:
              contador2=contador2+1
            else:
                print("su voto es erroneo")
                
        registrados.add(nombre)
    
        b=input('quiere agregar otro usuario marque "sii"\n')
                                
    else:
        print("Usuario o contraseña incorrecta.")

print('''Andres Carrascar tuvo una totalidad de ''', contador, '''votos
      Carlos Medina tuvo una totalidad de ''', contador1, '''votos
      Johan Cortez tuvo una totalidad de ''', contador2, 'votos')
