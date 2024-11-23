import csv

# Variables de usuario
L_contenido = []  # Lista para almacenar el contenido (películas, series, etc.)

# Diccionarios para almacenar clientes y administrador
V_cliente = {"Laura": {"contraseña": "A1b2C3"}, 
             "Juank": {"contraseña": "X9y8Z7"}, 
             "Milena": {"contraseña": "M4n5P6"}, 
             "Catalina": {"contraseña": "Q1w2E3"}, 
             "James": {"contraseña": "R10tY6"}}

V_admin = {"admi": {"contraseña": "adm000"}}

# Función para verificar las credenciales de usuario (admin o cliente)
def verificar_credenciales(usuario, contraseña, tipo):
    if tipo == "admin":
        if usuario in V_admin and V_admin[usuario]["contraseña"] == contraseña:
            return True
    elif tipo == "cliente":
        if usuario in V_cliente and V_cliente[usuario]["contraseña"] == contraseña:
            return True
    return False

# Menú principal
def menu():
    a = int(input('''Bienvenidos a Netflix
                        Desea ingresar como:
                            1. Administrador
                            2. Cliente
                        Ingrese su opción: '''))
    match a:
        case 1:
            administrador()
        case 2:
            cliente()

# Función para el administrador
def administrador():
    usuario = input("Por favor ingrese su nombre de usuario de administrador: \n")
    contraseña = input("Ingrese su contraseña: \n")
    
    if verificar_credenciales(usuario, contraseña, "admin"):
        b = int(input('''Has ingresado como administrador
                ¿Qué deseas hacer?
                    1. Eliminar cuentas
                    2. Crear nuevo usuario
                    3. Agregar nuevo contenido
                    4. Editar contenido
                    5. Eliminar contenido
                    6. Ver lista de contenido
                Ingrese su opción: '''))
        match b:
            case 1:
                eliminar_cuentas()
            case 2:
                crear_usuario()
            case 3:
                agregar_contenido()
            case 4:
                editar_contenido()
            case 5:
                eliminar_contenido()
            case 6:
                ver_contenido()
    else:
        print("Usuario o contraseña de administrador incorrectos.")

# Función para clientes
def cliente():
    usuario = input("Ingrese su nombre de usuario: \n")
    contraseña = input("Ingrese su contraseña: \n")
    
    if verificar_credenciales(usuario, contraseña, "cliente"):
        print(f"Bienvenido {usuario}. Puedes ver y buscar contenido.")
        ver_contenido()
    else:
        print("Usuario o contraseña incorrectos.")

# Funciones del administrador
def eliminar_cuentas():
    usuario_a_eliminar = input("Ingrese el nombre del usuario que desea eliminar: \n")
    if usuario_a_eliminar in V_cliente:
        del V_cliente[usuario_a_eliminar]
        print(f"La cuenta de {usuario_a_eliminar} ha sido eliminada.")
    else:
        print("El usuario no existe.")

def crear_usuario():
    nuevo_usuario = input("Ingrese el nombre del nuevo usuario: \n")
    nueva_contraseña = input("Ingrese la contraseña del nuevo usuario: \n")
    V_cliente[nuevo_usuario] = {"contraseña": nueva_contraseña}
    print(f"El usuario {nuevo_usuario} ha sido creado con éxito.")

def agregar_contenido():
    titulo = input("Ingrese el título del contenido: \n")
    genero = input("Ingrese el género del contenido: \n")
    duracion = input("Ingrese la duración del contenido: \n")
    L_contenido.append({"titulo": titulo, "genero": genero, "duracion": duracion})
    print(f"El contenido '{titulo}' ha sido agregado.")

def editar_contenido():
    titulo_a_editar = input("Ingrese el título del contenido que desea editar: \n")
    for contenido in L_contenido:
        if contenido["titulo"] == titulo_a_editar:
            nuevo_titulo = input("Ingrese el nuevo título: \n")
            nuevo_genero = input("Ingrese el nuevo género: \n")
            nueva_duracion = input("Ingrese la nueva duración: \n")
            contenido.update({"titulo": nuevo_titulo, "genero": nuevo_genero, "duracion": nueva_duracion})
            print(f"El contenido '{nuevo_titulo}' ha sido actualizado.")
            return
    print("El contenido no fue encontrado.")

def eliminar_contenido():
    titulo_a_eliminar = input("Ingrese el título del contenido que desea eliminar: \n")
    for contenido in L_contenido:
        if contenido["titulo"] == titulo_a_eliminar:
            L_contenido.remove(contenido)
            print(f"El contenido '{titulo_a_eliminar}' ha sido eliminado.")
            return
    print("El contenido no fue encontrado.")

def ver_contenido():
    if not L_contenido:
        print("No hay contenido disponible.")
    else:
        print("Lista de contenido disponible:")
        for contenido in L_contenido:
            print(f"Título: {contenido['titulo']}, Género: {contenido['genero']}, Duración: {contenido['duracion']}")

# Ejecutar el menú
menu()
