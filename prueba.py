productos = [
    {"nombre": "Manzanas rojas", "tipo": "FRUTAS", "precio": 3.00, "unidad": "libra", "cantidad": 1},
    {"nombre": "Bananas", "tipo": "FRUTAS", "precio": 1.50, "unidad": "libra", "cantidad": 1},
    {"nombre": "Naranjas", "tipo": "FRUTAS", "precio": 4.00, "unidad": "docena", "cantidad": 12},
    {"nombre": "Fresas", "tipo": "FRUTAS", "precio": 5.00, "unidad": "caja", "cantidad": 1},
    {"nombre": "Mangos", "tipo": "FRUTAS", "precio": 2.50, "unidad": "unidad", "cantidad": 1},
    {"nombre": "Uvas verdes", "tipo": "FRUTAS", "precio": 4.00, "unidad": "libra", "cantidad": 1},
    {"nombre": "Piña", "tipo": "FRUTAS", "precio": 3.00, "unidad": "unidad", "cantidad": 1},
    {"nombre": "Kiwis", "tipo": "FRUTAS", "precio": 3.50, "unidad": "paquete", "cantidad": 4},
    {"nombre": "Papayas", "tipo": "FRUTAS", "precio": 3.00, "unidad": "unidad", "cantidad": 1},
    {"nombre": "Peras", "tipo": "FRUTAS", "precio": 2.50, "unidad": "libra", "cantidad": 1},
    {"nombre": "Zanahorias", "tipo": "VERDURAS", "precio": 2.00, "unidad": "libra", "cantidad": 1},
    {"nombre": "Tomates", "tipo": "VERDURAS", "precio": 2.50, "unidad": "libra", "cantidad": 1},
    {"nombre": "Lechuga", "tipo": "VERDURAS", "precio": 2.00, "unidad": "cabeza", "cantidad": 1},
    {"nombre": "Papas", "tipo": "VERDURAS", "precio": 3.00, "unidad": "bolsa", "cantidad": 5},
    {"nombre": "Cebolla", "tipo": "VERDURAS", "precio": 1.50, "unidad": "libra", "cantidad": 1},
    {"nombre": "Pimientos rojos", "tipo": "VERDURAS", "precio": 3.00, "unidad": "libra", "cantidad": 1},
    {"nombre": "Brócoli", "tipo": "VERDURAS", "precio": 2.50, "unidad": "libra", "cantidad": 1},
    {"nombre": "Pechuga de pollo", "tipo": "CÁRNICOS", "precio": 4.50, "unidad": "libra", "cantidad": 1},
    {"nombre": "Carne de res molida", "tipo": "CÁRNICOS", "precio": 6.00, "unidad": "libra", "cantidad": 1},
    {"nombre": "Chuletas de cerdo", "tipo": "CÁRNICOS", "precio": 5.00, "unidad": "libra", "cantidad":1}
]

print ("""MENÚ DE INVENTARIO FRUVER ECOFRESCO
                    MARQUE: 1. MOSTRAR TODOS LOS PRODUCTOS
                            2. MOSTRAR PRODUCTOS DE MAYOR CANTIDAD
                            3. MOSTRAR PRODUCTOS DE MAYOR PRECIO
                            4. MOSTRAR PRODUCTOS DE MENOR PRECIO
                            5. MOSTRAR EL VALOR TOTAL DEL INVENTARIO
                            6. MODULO DE VENTAS
                            7. SALIR""")

while True:
    op = ['1', '2', '3', '4', '5', '6', '7']
    opcion = input('Seleccione una opción: ')
    if opcion in op:
        if opcion == "1":
            # Imprimir los detalles de cada producto
            for producto in productos:
                print(f"{producto['nombre']}")
                print(f"Tipo: {producto['tipo']}")
                print(f"Precio: {producto['precio']:.2f}")
                print(f"Unidad: {producto['unidad']}")
                print(f"Cantidad: {producto['cantidad']}")
                print('-' * 40)
    #     elif opcion == "2":
    #         break
    #     elif opcion == "3":
    #         break
    #     elif opcion == "4":
    #         break
    #     elif opcion == "5":
    #         break
    #     elif opcion == "6":
    #         break
    #     elif opcion == "7":
    #         break        
        
    # else:
    #     print('DIGITE UNA OPCIÓN ADECUADA')




























































