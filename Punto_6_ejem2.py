'''Se requiere diseñar un programa mediante Python y POO, que satisfaga la siguiente situación: Una empresa requiere implementar un sistema de información donde se encuentren todos sus empleados y visitantes con los siguientes datos (código empleado, apellidos, nombres, # documento, área de trabajo (seguridad, servicios generales, administrativo, auxiliar o visitante), hora de ingreso, temperatura de ingreso °C, hora de salida, temperatura de salida °C). Su programa debe tener la posibilidad de establecer las clases necesarias con sus atributos y métodos para lograr: aceptar el ingreso de información según requerimientos, editar la información cuando sea necesaria, eliminar usuarios que ya no pertenezcan a la empresa, hacer búsquedas de empleados o visitantes teniendo en cuenta los siguientes criterios: mostrar nombre y apellidos de usuarios que tengan temperatura mayor a 37.5°C, por cargo dentro de la empresa o visitantes, por hora de llegada y por hora de salida. Además, su programa debe enviar alertas en pantalla donde establezca un mensaje de que algún empleado esta por arriba de 38°C en la medición de su temperatura.'''

class Persona:
    def __init__(self, codigo, apellidos, nombres, documento, area, hora_ingreso, temp_ingreso, hora_salida, temp_salida):
        self.codigo = codigo
        self.apellidos = apellidos
        self.nombres = nombres
        self.documento = documento
        self.area = area
        self.hora_ingreso = hora_ingreso
        self.temp_ingreso = temp_ingreso
        self.hora_salida = hora_salida
        self.temp_salida = temp_salida

    def mostrar_info(self):
        return (f"Código: {self.codigo}, Nombre: {self.nombres} {self.apellidos}, Documento: {self.documento}, "
                f"Área: {self.area}, Hora de Ingreso: {self.hora_ingreso}, Temperatura Ingreso: {self.temp_ingreso}°C, "
                f"Hora de Salida: {self.hora_salida}, Temperatura Salida: {self.temp_salida}°C")

    def editar_info(self, apellidos=None, nombres=None, documento=None, area=None, hora_ingreso=None, temp_ingreso=None, hora_salida=None, temp_salida=None):
        if apellidos is not None: self.apellidos = apellidos
        if nombres is not None: self.nombres = nombres
        if documento is not None: self.documento = documento
        if area is not None: self.area = area
        if hora_ingreso is not None: self.hora_ingreso = hora_ingreso
        if temp_ingreso is not None: self.temp_ingreso = temp_ingreso
        if hora_salida is not None: self.hora_salida = hora_salida
        if temp_salida is not None: self.temp_salida = temp_salida

class SistemaInformacion:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, persona):
        self.usuarios.append(persona)
        if persona.temp_ingreso > 38.0:
            print(f"Alerta: {persona.nombres} {persona.apellidos} tiene una temperatura de ingreso de {persona.temp_ingreso}°C, por encima de 38°C.")

    def editar_usuario(self, codigo, **kwargs):
        usuario = self.buscar_por_codigo(codigo)
        if usuario:
            usuario.editar_info(**kwargs)
            print("Información actualizada correctamente.")
        else:
            print("Usuario no encontrado.")

    def eliminar_usuario(self, codigo):
        usuario = self.buscar_por_codigo(codigo)
        if usuario:
            self.usuarios.remove(usuario)
            print("Usuario eliminado correctamente.")
        else:
            print("Usuario no encontrado.")

    def buscar_por_codigo(self, codigo):
        for usuario in self.usuarios:
            if usuario.codigo == codigo:
                return usuario
        return None

    def mostrar_temperatura_mayor_37_5(self):
        print("\nUsuarios con temperatura de ingreso mayor a 37.5°C:")
        for usuario in self.usuarios:
            if usuario.temp_ingreso > 37.5:
                print(f"{usuario.nombres} {usuario.apellidos} - Temperatura Ingreso: {usuario.temp_ingreso}°C")

    def buscar_por_area(self, area):
        print(f"\nUsuarios en el área: {area}")
        for usuario in self.usuarios:
            if usuario.area.lower() == area.lower():
                print(usuario.mostrar_info())

    def buscar_por_hora_llegada(self, hora):
        print(f"\nUsuarios con hora de ingreso: {hora}")
        for usuario in self.usuarios:
            if usuario.hora_ingreso == hora:
                print(usuario.mostrar_info())

    def buscar_por_hora_salida(self, hora):
        print(f"\nUsuarios con hora de salida: {hora}")
        for usuario in self.usuarios:
            if usuario.hora_salida == hora:
                print(usuario.mostrar_info())

    def mostrar_informacion(self):
        print("\nInformación de todos los usuarios:")
        for usuario in self.usuarios:
            print(usuario.mostrar_info())

# Ejemplo de uso
def menu():
    sistema = SistemaInformacion()
    
    while True:
        print("\n--- Sistema de Información de Empleados y Visitantes ---\n")
        print("1. Agregar Usuario")
        print("2. Editar Usuario")
        print("3. Eliminar Usuario")
        print("4. Mostrar Usuarios con Temperatura de Ingreso > 37.5°C")
        print("5. Buscar por Área")
        print("6. Buscar por Hora de Ingreso")
        print("7. Buscar por Hora de Salida")
        print("8. Mostrar Información de Todos los Usuarios")
        print("9. Salir")
        opcion = input("\nSeleccione una opción: ")
        print('')
        print('-'*30)
        print('')
        
        if opcion == "1":
            agregar_usuario(sistema)
        elif opcion == "2":
            codigo = input("Ingrese el código del usuario a editar: ")
            editar_usuario(sistema, codigo)
        elif opcion == "3":
            codigo = input("Ingrese el código del usuario a eliminar: ")
            sistema.eliminar_usuario(codigo)
        elif opcion == "4":
            sistema.mostrar_temperatura_mayor_37_5()
        elif opcion == "5":
            area = input("Ingrese el área de trabajo (seguridad, servicios generales, administrativo, auxiliar o visitante.): ")
            sistema.buscar_por_area(area)
        elif opcion == "6":
            hora = input("Ingrese la hora de ingreso (HH:MM): ")
            sistema.buscar_por_hora_llegada(hora)
        elif opcion == "7":
            hora = input("Ingrese la hora de salida (HH:MM): ")
            sistema.buscar_por_hora_salida(hora)
        elif opcion == "8":
            sistema.mostrar_informacion()
        elif opcion == "9":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def agregar_usuario(sistema):
    codigo = input("Ingrese el código del usuario: ")
    apellidos = input("Ingrese los apellidos: ")
    nombres = input("Ingrese los nombres: ")
    documento = input("Ingrese el número de documento: ")
    area = input("Ingrese el área de trabajo (seguridad, servicios generales, administrativo, auxiliar o visitante): ")
    hora_ingreso = input("Ingrese la hora de ingreso (HH:MM): ")
    temp_ingreso = float(input("Ingrese la temperatura de ingreso en °C: "))
    hora_salida = input("Ingrese la hora de salida (HH:MM): ")
    temp_salida = float(input("Ingrese la temperatura de salida en °C: "))
    
    persona = Persona(codigo, apellidos, nombres, documento, area, hora_ingreso, temp_ingreso, hora_salida, temp_salida)
    sistema.agregar_usuario(persona)
    print("Usuario agregado exitosamente.")

def editar_usuario(sistema, codigo):
    apellidos = input("Ingrese los nuevos apellidos (deje en blanco para no cambiar): ") or None
    nombres = input("Ingrese los nuevos nombres (deje en blanco para no cambiar): ") or None
    documento = input("Ingrese el nuevo número de documento (deje en blanco para no cambiar): ") or None
    area = input("Ingrese el nuevo área de trabajo (deje en blanco para no cambiar): ") or None
    hora_ingreso = input("Ingrese la nueva hora de ingreso (HH:MM, deje en blanco para no cambiar): ") or None
    temp_ingreso = input("Ingrese la nueva temperatura de ingreso en °C (deje en blanco para no cambiar): ")
    hora_salida = input("Ingrese la nueva hora de salida (HH:MM, deje en blanco para no cambiar): ") or None
    temp_salida = input("Ingrese la nueva temperatura de salida en °C (deje en blanco para no cambiar): ")
    
    sistema.editar_usuario(codigo, 
                           apellidos=apellidos,
                           nombres=nombres,
                           documento=documento,
                           area=area,
                           hora_ingreso=hora_ingreso,
                           temp_ingreso=float(temp_ingreso) if temp_ingreso else None,
                           hora_salida=hora_salida,
                           temp_salida=float(temp_salida) if temp_salida else None)

menu()