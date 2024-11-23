productos = [
    "FRUTAS":{
        {"nombre": "Manzanas rojas",  "precio": 3.00, "unidad": "libra", "cantidad": 1},
        {"nombre": "Bananas",  "precio": 1.50, "unidad": "libra", "cantidad": 1},
        {"nombre": "Naranjas",  "precio": 4.00, "unidad": "docena", "cantidad": 12},
        {"nombre": "Fresas",  "precio": 5.00, "unidad": "caja", "cantidad": 1},
        {"nombre": "Mangos",  "precio": 2.50, "unidad": "unidad", "cantidad": 1},
        {"nombre": "Uvas verdes",  "precio": 4.00, "unidad": "libra", "cantidad": 1},
        {"nombre": "Piña",  "precio": 3.00, "unidad": "unidad", "cantidad": 1},
        {"nombre": "Kiwis",  "precio": 3.50, "unidad": "paquete", "cantidad": 4},
        {"nombre": "Papayas",  "precio": 3.00, "unidad": "unidad", "cantidad": 1},
        {"nombre": "Peras",  "precio": 2.50, "unidad": "libra", "cantidad": 1},
    },
     "VERDURAS":{
        {"nombre": "Zanahorias",  "precio": 2.00, "unidad": "libra", "cantidad": 1},
        {"nombre": "Tomates",  "precio": 2.50, "unidad": "libra", "cantidad": 1},
        {"nombre": "Lechuga",  "precio": 2.00, "unidad": "cabeza", "cantidad": 1},
        {"nombre": "Papas",  "precio": 3.00, "unidad": "bolsa", "cantidad": 5},
        {"nombre": "Cebolla",  "precio": 1.50, "unidad": "libra", "cantidad": 1},
        {"nombre": "Pimientos rojos",  "precio": 3.00, "unidad": "libra", "cantidad": 1},
        {"nombre": "Brócoli",  "precio": 2.50, "unidad": "libra", "cantidad": 1},
    },
     "CÁRNICOS":{
        {"nombre": "Pechuga de pollo",  "precio": 4.50, "unidad": "libra", "cantidad": 1},
        {"nombre": "Carne de res molida",  "precio": 6.00, "unidad": "libra", "cantidad": 1},
        {"nombre": "Chuletas de cerdo",  "precio": 5.00, "unidad": "libra", "cantidad":1}
    }
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
##                print(f"Tipo: {producto['tipo']}")
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



































































