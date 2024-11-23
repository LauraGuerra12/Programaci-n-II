import datetime

L_PRECIO_MOTO = 500
L_PRECIO_CARRO = 1000

vehiculos = []


def calcular_duracion(entrada, salida):
    formato = "%H:%M"  
    try:
        v_entrada_dt = datetime.datetime.strptime(entrada, formato)
        v_salida_dt = datetime.datetime.strptime(salida, formato)
        if v_salida_dt < v_entrada_dt:
            v_salida_dt += datetime.timedelta(days=1)  
        duracion = (v_salida_dt - v_entrada_dt).total_seconds() / 60  
        return int(duracion)
    except ValueError:
        print("Formato de hora incorrecto. Asegúrate de ingresar la hora en formato Hor:Min (24 horas).")
        return None

def calcular_precio(duracion, tipo):
    fracciones = duracion // 15
    if duracion % 15 != 0:
        fracciones += 1
    if tipo == 'MOTO':
        return fracciones * L_PRECIO_MOTO
    elif tipo == 'CARRO':
        return fracciones * L_PRECIO_CARRO

def registrar_entrada():
    tipo = input("Ingrese el tipo de vehículo (MOTO/CARRO): ").upper()
    if tipo not in ['MOTO', 'CARRO']:
        print("Tipo de vehículo inválido. Debe ser MOTO o CARRO.")
        return

    placa = input("Ingrese la placa del vehículo: ").upper()
    hora_entrada = input("Ingrese la hora de entrada (Hor:Min en formato 24 horas): ")

    if calcular_duracion(hora_entrada, hora_entrada) is None:
        return

    vehiculo = {
        'tipo': tipo,
        'placa': placa,
        'hora_entrada': hora_entrada,
        'hora_salida': None,
        'duracion': None,
        'precio': None
    }
    vehiculos.append(vehiculo)
    print(f"Vehículo {tipo} con placa {placa} registrado a las {hora_entrada}.\n")

def registrar_salida():
    placa = input("Ingrese la placa del vehículo que va a salir: ").upper()

    for vehiculo in vehiculos:
        if vehiculo['placa'] == placa and vehiculo['hora_salida'] is None:
            hora_salida = input("Ingrese la hora de salida (Hor:Min en formato 24 horas): ")
            duracion = calcular_duracion(vehiculo['hora_entrada'], hora_salida)

            if duracion is None:
                return

            vehiculo['hora_salida'] = hora_salida
            vehiculo['duracion'] = duracion
            vehiculo['precio'] = calcular_precio(duracion, vehiculo['tipo'])

            print(f"Vehículo {vehiculo['tipo']} con placa {vehiculo['placa']} ha permanecido {duracion} minutos.")
            print(f"El valor a pagar es: ${vehiculo['precio']}.\n")
            return
    print("Vehículo no encontrado o ya registrado como salido.\n")

def mostrar_resumen():
    total_carros = sum(1 for v in vehiculos if v['tipo'] == 'CARRO')
    total_motos = sum(1 for v in vehiculos if v['tipo'] == 'MOTO')
    dinero_carros = sum(v['precio'] for v in vehiculos if v['tipo'] == 'CARRO' and v['precio'] is not None)
    dinero_motos = sum(v['precio'] for v in vehiculos if v['tipo'] == 'MOTO' and v['precio'] is not None)

    print(f"Resumen del día:")
    print(f"Total de carros ingresados: {total_carros}")
    print(f"Total de motos ingresadas: {total_motos}")
    print(f"Dinero recaudado por carros: ${dinero_carros}")
    print(f"Dinero recaudado por motos: ${dinero_motos}\n")

def mostrar_placas():
    if not vehiculos:
        print("No hay vehículos registrados aún.")
        return
    
    print("Placas de los vehículos ingresados:")
    for vehiculo in vehiculos:
        print(f"Placa: {vehiculo['placa']} - Tipo: {vehiculo['tipo']}")
    print()

def menu():
    while True:
        print("1. Registrar entrada de vehículo")
        print("2. Registrar salida de vehículo")
        print("3. Mostrar resumen del parqueadero")
        print("4. Mostrar placas de vehículos ingresados")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_entrada()
        elif opcion == "2":
            registrar_salida()
        elif opcion == "3":
            mostrar_resumen()
        elif opcion == "4":
            mostrar_placas()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

menu()
