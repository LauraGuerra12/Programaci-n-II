'''Realice un diagrama de clases y objetos para el siguiente problema:

Una empresa requiere de un sistema de gestion de inventario para las tiendas, sabiendo que venden diferentes productos. Cada producto tiene un nombre, un precio y una cantidad en stock.Existen productos que puedes ser electronicos y otros son alimentos. Para los electronicos, ademas de los atributos generales de un producto, se debe tener en cuenta tener un atributo de garantia. Para los alimentos, ademas de los atributos generales de un producto, se debe tener en cuenta tener un atributo de fecha de vencimiento. El sistema debe permitir agregar productos al inventario, mostrar productos en stock y realizar ventas actualizando el inventario. Para su implementacion evidencie el uso de herencia y encapsulamiento. Tambien archivos CSV'''

import csv
#import pandas as pd   #No fui capaz de importar pandas
from datetime import datetime

class L_Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class L_Electronico(L_Producto):
    def __init__(self, nombre, precio, cantidad, garantia):
        super().__init__(nombre, precio, cantidad)
        self.garantia = garantia

class L_Alimento(L_Producto):
    def __init__(self, nombre, precio, cantidad, fecha_vencimiento):
        super().__init__(nombre, precio, cantidad)
        self.fecha_vencimiento = fecha_vencimiento

class L_Inventario:
    def __init__(self):
        self.productos = []

    def vg_agregar_producto(self, producto):
        self.productos.append(producto)
        self.vg_exportar_a_csv()

    def vg_mostrar_productos(self):
        for producto in self.productos:
            if isinstance(producto, L_Electronico):
                print(f"Nombre: {producto.nombre} |, Tipo de Producto: Electronico |, Precio: {producto.precio} |, Cantidad: {producto.cantidad} |, Garantia/Fecha de Vencimiento: {producto.garantia} meses")
            elif isinstance(producto, L_Alimento):
                print(f"Nombre: {producto.nombre} |, Tipo de Producto: Alimento |, Precio: {producto.precio} |, Cantidad: {producto.cantidad} |, Fecha de Vencimiento: {producto.fecha_vencimiento}")
            else:
                print(f"Nombre: {producto.nombre} | Precio: {producto.precio} | Cantidad: {producto.cantidad}")

    def vg_vender_producto(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto and producto.cantidad >= cantidad:
                producto.cantidad -= cantidad
                self.vg_exportar_a_csv()
                print(f"Venta realizada: {cantidad} de {nombre_producto}")
                return
        print("Venta no realizada: producto no encontrado o cantidad insuficiente")

    def vg_exportar_a_csv(self, nombre_archivo='./2225078_inventario.csv'):
        with open(nombre_archivo, mode='w') as archivo:
            escritor_csv = csv.writer(archivo, delimiter='|')
            escritor_csv.writerow(['Nombre', 'Tipo de Producto', 'Precio', 'Cantidad', 'Garantia/Fecha de Vencimiento'])
            for producto in self.productos:
                if isinstance(producto, L_Electronico):
                    escritor_csv.writerow([producto.nombre, 'Electronico', producto.precio, producto.cantidad, f'{producto.garantia} meses'])
                elif isinstance(producto, L_Alimento):
                    escritor_csv.writerow([producto.nombre, 'Alimento', producto.precio, producto.cantidad, producto.fecha_vencimiento])
                else:
                    escritor_csv.writerow([producto.nombre, 'Producto', producto.precio, producto.cantidad, ''])

def menu():
    inventario = L_Inventario()
    while True:
        print("\n--- Menú de Inventario ---\n")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Realizar venta")
        print("4. Salir")
        opcion = input("\nSeleccione una opción: ")
        print('')
        print('-'*30)
        print('')

        if opcion == '1':
            tipo = input("Tipo de producto (1. Electrónico, 2. Alimento): ")
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))

            if tipo == '1':
                garantia = int(input("Garantía (meses): "))
                producto = L_Electronico(nombre, precio, cantidad, garantia)
            elif tipo == '2':
                fecha_vencimiento = input("Fecha de vencimiento (DD-MM-YYYY): ")
                producto = L_Alimento(nombre, precio, cantidad, fecha_vencimiento)
            else:
                print("Tipo de producto no válido.")
                continue

            inventario.vg_agregar_producto(producto)
            print("Producto agregado al inventario y guardado en CSV.")

        elif opcion == '2':
            inventario.vg_mostrar_productos()

        elif opcion == '3':
            nombre_producto = input("Nombre del producto a vender: ")
            cantidad = int(input("Cantidad: "))
            inventario.vg_vender_producto(nombre_producto, cantidad)

        elif opcion == '4':
            print("Saliendo del sistema de inventario.")
            exit()

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

if __name__ == "__main__":
    menu()


