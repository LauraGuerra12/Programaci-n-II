#Netflix
#Laura Valentina Guerra Cepeda
import csv
L_contenido = []

V_cliente = {"Laura":{"contraseña": "A1b2C3", "lvg_tipo_cuen": "premium"}, "Juank":{"contraseña":"X9y8Z7", "lvg_tipo_cuen": "estandar"}, "Milena":{"contraseña":"M4n5P6", "lvg_tipo_cuen": "estandar"}, "Catalina":{"contraseña":"Q1w2E3", "lvg_tipo_cuen": "basica"}, "James":{"contraseña":"R10tY6", "lvg_tipo_cuen": "premium"}}
V_admin = {"admi":{"contraseña": "adm000"}}

def menu():
    la = int(input('''Bienvenidos a Netflix
                        Desea ingresar como:
                            1 Administrador
                            2 Cliente
                            Ingrese su opción: '''))
    
    match la:
        case 1:
            Administrador()
        case 2:
            Cliente()

def Administrador():
    la = "si"
    while la == "si":
        L_usu = input("Por favor ingrese su nombre de usuario: \n")
        if L_usu in V_admin:
            L_passw = input("Ingrese su contraseña: \n")
            if L_passw == V_admin[L_usu]["contraseña"]:
                lb = int(input('''Has ingresado como administrador
                                ¿Qué deseas hacer?
                                    1. Eliminar cuentas
                                    2. Crear nuevo usuario
                                    3. Agregar nuevo contenido
                                    4. Editar contenido
                                    5. Eliminar contenido
                                    6. Ver lista de contenido
                                    Ingrese su opción: '''))
                match lb:
                    case 1:
                        val_elim_cuentas()
                    case 2:
                        val_crear_usuario()
                    case 3:
                        val_agre_contenido()
                    case 4:
                        val_edi_contenido()
                    case 5:
                        val_elim_contenido()
                    case 6:
                        val_ver_contenido()
            else:
                la = input("Contraseña incorrecta. Si desea volver a ingresar marque 'si', de lo contrario presione Enter para salir.\n")
        else:
            la = input("Usuario erróneo. Si desea volver a intentar marque 'si', de lo contrario presione Enter para salir.\n")

def val_elim_cuentas():
    ce_usu_a_elim = input("Ingrese el nombre del usuario que desea eliminar: \n")
    if ce_usu_a_elim in V_cliente:
        del V_cliente[ce_usu_a_elim]
        print(f"La cuenta de {ce_usu_a_elim} ha sido eliminada.")
    else:
        print("El usuario no existe.")

def val_crear_usuario():
    gu_new_usu = input("Ingrese el nombre del nuevo usuario: \n")
    gu_new_passw = input("Ingrese la contraseña del nuevo usuario: \n")
    V_cliente[gu_new_usu] = {"contraseña": gu_new_passw}
    print(f"El usuario {nuevo_usuario} ha sido creado con éxito.")

def val_agre_contenido():
    l_titu = input("Ingrese el título del contenido: \n")
    l_gene = input("Ingrese el género del contenido: \n")
    L_contenido.append({"titulo": l_titu, "genero": l_gene})
    print(f"El contenido '{titulo}' ha sido agregado.")
    
def val_edi_contenido():
    cep_titu_a_edi = input('Ingrese el título del contenido que desea editar')
    for contenido in L_contenido:
        if contenido["titulo"] == titulo_a_editar:
            Laur_new_titu = input("Ingrese el nuevo título: \n")
            Laur_new_gene = input("Ingrese el nuevo género: \n")
            L_contenido.update({"titulo": Laur_new_titu, "genero": Laur_new_gene})
            print(f"El contenido '{Laur_new_titu}' ha sido actualizado.")
            return
    print("El contenido no fue encontrado.")

def val_elim_contenido():
    gue_titu_a_elim = input("Ingrese el título del contenido que desea eliminar: \n")
    for contenido in L_contenido:
        if contenido["titulo"] == gue_titu_a_elim:
            L_contenido.remove(contenido)
            print(f"El contenido '{titulo_a_eliminar}' ha sido eliminado.")
            return
    print("El contenido no fue encontrado.")

def val_ver_contenido():
    if not L_contenido:
        print("No hay contenido disponible.")
    else:
        print("Lista de contenido disponible:")
        for contenido in L_contenido:
            print(f"Título: {contenido['titulo']}, Género: {contenido['genero']}")



def Cliente():
    while la_a == "si":
        Lv_usu = input("Ingrese su nombre de usuario: \n")
        if Lv_usu in V_cliente:
            Lv_passw = input("Ingrese su contraseña: \n")
            if Lv_passw == V_cliente[Lv_usu]["contraseña"]:
                lb_b = int(input('''Bienvenido a Netflix
                                ¿Qué deseas hacer?
                                    1. Cambiar nombre 
                                    2. Cambiar contraseña
                                    3. Eliminar cuenta
                                    4. Pagar
                                    5. Buscar contenido
                                    6. Agregar a favoritos
                                    Ingrese su opción: '''))      
                match lb_b:
                        case 1:
                            val_camb_nom()
                        case 2:
                             val_camb_passw()
                        case 3:
                            val_elim_cuenta()
                        case 4:
                            val_pagar()
                        case 5:
                            val_buscar_contenido()
                        case 6:
                            val_agreg_fav()
            else:
                la = input("Contraseña incorrecta. Si desea volver a ingresar marque 'si', de lo contrario presione Enter para salir.\n")
        else:
            la = input("Usuario erróneo. Si desea volver a intentar marque 'si', de lo contrario presione Enter para salir.\n")


def val_camb_nom():
    lg_new_nombre = input("Ingrese su nuevo nombre de usuario: \n")
    if lg_new_nombre not in V_cliente:
        V_cliente[lg_new_nombre] = V_cliente.pop()
        print(f"Nombre de usuario cambiado exitosamente a {nuevo_nombre}.")
    else:
        print("El nombre de usuario ya está en uso.")

def val_camb_passw():
    lg_new_contraseña = input("Ingrese su nueva contraseña (alfanumérica de 6 caracteres): \n")
    if len(lg_new_contraseña) == 6 and lg_new_contraseña.isalnum():
        V_cliente[Lv_usu]["contraseña"] = lg_new_contraseña
        print("Contraseña cambiada exitosamente.")
    else:
        print("La contraseña debe ser alfanumérica y tener 6 caracteres.")

def val_elim_cuenta():
    g_confirmacion = input("¿Está seguro de que desea eliminar su cuenta? (si/no): \n")
    if g_confirmacion.lower() == "si":
        del V_cliente[Lv_usu]
        print(f"La cuenta de {Lv_usu} ha sido eliminada.")

def val_pagar():
    lvg_tipo_cuen = input("Ingrese el tipo de cuenta que desea (basica, estandar, premium): \n").lower()
    precios = {"basica": 1000, "estandar": 2000, "premium": 3000}
    
    if lvg_tipo_cuen in precios:
        print(f"Ha seleccionado el tipo de cuenta {lvg_tipo_cuen.capitalize()}. Debe pagar {precios[lvg_tipo_cuen]} pesos.")  #capitalize() convierte la primera letra de una cadena en mayúsculas y el resto de los caracteres en minúsculas
        V_cliente[Lv_usu]["lvg_tipo_cuen"] = lvg_tipo_cuen
        print(f"Su cuenta ha sido actualizada a {lvg_tipo_cuen.capitalize()}.")
    else:
        print("Tipo de cuenta no válido.")











def guardar(): #Almacena en CSV. Recuerde que el archivo debe estar cerrado para guardar nuevos datos
    with open('C:/Users/Laura/OneDrive - Universidad Industrial de Santander/CUARTO SEMESTRE/PROGRAMACION II/CSV/ContenidoNetflix_LG.csv', 'w',  newline='') as Netflix:
        escri=csv.writer(Netflix, delimiter=';')   
        escri.writerows(L_contenido)
    print('Datos almacenados con éxito\n')

Lg_op=int(input('Marque 3: para agregar contenido, 4: para editar contenido, 5: para eliminar contenido, 6: para ver contenido\n'))


    
while Lg_op==3 or Lg_op==4 or Lg_op==5 or Lg_op==6:
    #Lectura de CSV. 
    with open('C:/Users/Laura/OneDrive - Universidad Industrial de Santander/CUARTO SEMESTRE/PROGRAMACION II/CSV/ContenidoNetflix_LG.csv', 'w',  newline='') as Netflix:
        v_leer = csv.reader(Netflix, delimiter=';')
        L_contenido = list(v_leer)
        
    if Lg_op==3:
      print('###### AGREGAR CONTENIDO ######')
      print('\n')
      val_agre_contenido()
      
    elif Lg_op==4:
      print('###### EDITAR CONTENIDO ######')
      print('\n')
      val_edi_contenido()

    elif Lg_op==5:
      print('###### ELIMINAR CONTENIDO ######')
      print('\n')
      val_elim_contenido()

    elif Lg_op==6:
      print('###### VER CONTENIDO ######')
      print('\n')
      val_ver_contenido()
    print('\n')
    Lg_op=int(input('Marque 3: para agregar contenido, 4: para editar contenido, 5: para eliminar contenido, 6: para ver contenido\n'))

    




menu() 
