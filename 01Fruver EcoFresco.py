class Producto:
    def __init__(self, nombre, categoria, precio, cantidad, unidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad
        self.unidad = unidad

    def __str__(self):
        return (f"-{self.nombre}\n"
                f"\t\tPrecio: ${self.precio:.0f} por {self.unidad}\n"
                f"\t\tCantidad: {self.cantidad} {self.unidad}(s)")

    def calcular_precio_total(self, cantidad):
        return self.precio * cantidad


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("PRODUCTOS")
        categorias = {"Frutas": [], "Verduras": [], "Cárnicos": []}
        
        for producto in self.productos:
            categorias[producto.categoria].append(producto)

        for categoria, productos in categorias.items():
            print(f"\n\t{categoria.upper()}")
            for producto in productos:
                print(f"\t{producto}")

    def obtener_producto_mayor_cantidad(self):
        return max(self.productos, key=lambda p: p.cantidad)

    def obtener_producto_mayor_precio(self):
        return max(self.productos, key=lambda p: p.precio)

    def obtener_producto_menor_precio(self):
        return min(self.productos, key=lambda p: p.precio)

    def calcular_valor_total(self):
        return sum(p.calcular_precio_total(p.cantidad) for p in self.productos)

    def vender_producto(self, nombre, cantidad_vendida):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                if producto.cantidad >= cantidad_vendida:
                    producto.cantidad -= cantidad_vendida
                    total_a_pagar = producto.calcular_precio_total(cantidad_vendida)
                    print(f"Venta realizada: {cantidad_vendida} {producto.unidad}(s) de {producto.nombre}.")
                    print(f"Precio a pagar: ${total_a_pagar:.2f}")
                else:
                    print("No hay suficiente cantidad en inventario.")
                return
        print("Producto no encontrado en el inventario.")


def inicializar_inventario():
    inventario = Inventario()
    productos = [
        ("Manzanas rojas", "Frutas", 3000, 1, "libra"),
        ("Bananas", "Frutas", 1500, 1, "libra"),
        ("Naranjas", "Frutas", 4000, 12, "unidades"),
        ("Fresas", "Frutas", 5000, 1, "libra"),
        ("Mangos", "Frutas", 2500, 1, "unidad"),
        ("Uvas verdes", "Frutas", 4000, 1, "libra"),
        ("Piña", "Frutas", 3000, 1, "unidad"),
        ("Kiwis", "Frutas", 3500, 4, "paquete"),
        ("Papayas", "Frutas", 3000, 1, "unidad"),
        ("Peras", "Frutas", 2500, 1, "libra"),
        ("Zanahorias", "Verduras", 2000, 1, "libra"),
        ("Tomates", "Verduras", 2500, 1, "libra"),
        ("Lechuga", "Verduras", 2000, 1, "cabeza"),
        ("Papas", "Verduras", 3000, 5, "bolsa"),
        ("Cebolla", "Verduras", 1500, 1, "libra"),
        ("Pimientos rojos", "Verduras", 3000, 1, "libra"),
        ("Brócoli", "Verduras", 2500, 1, "libra"),
        ("Pechuga de pollo", "Cárnicos", 4500, 1, "libra"),
        ("Carne de res molida", "Cárnicos", 6000, 1, "libra"),
        ("Chuletas de cerdo", "Cárnicos", 5000, 1, "libra"),
    ]
    for nombre, categoria, precio, cantidad, unidad in productos:
        inventario.agregar_producto(Producto(nombre, categoria, precio, cantidad, unidad))
    
    return inventario


def mostrar_menu(inventario):
        print ("""MENÚ DE INVENTARIO FRUVER ECOFRESCO
                    MARQUE: 1. MOSTRAR TODOS LOS PRODUCTOS
                            2. MOSTRAR PRODUCTOS DE MAYOR PRECIO
                            3. MOSTRAR PRODUCTOS DE MENOR PRECIO
                            4. MOSTRAR PRODUCTOS DE MAYOR CANTIDAD
                            5. MOSTRAR EL VALOR TOTAL DEL INVENTARIO
                            6. VENDER UN PRODUCTO
                            7. SALIR""")
        opcion = input("Ingrese la opción: ")
        
        if opcion == '1':
            inventario.mostrar_productos()
        elif opcion == '2':
            producto = inventario.obtener_producto_mayor_cantidad()
            print(f"Producto con mayor cantidad: {producto}")
        elif opcion == '3':
            producto = inventario.obtener_producto_mayor_precio()
            print(f"Producto con mayor precio: {producto}")
        elif opcion == '4':
            producto = inventario.obtener_producto_menor_precio()
            print(f"Producto con menor precio: {producto}")
        elif opcion == '5':
            total = inventario.calcular_valor_total()
            print(f"Valor total del inventario: ${total:.2f}")
        elif opcion == '6':
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = float(input("Ingrese la cantidad a vender: "))
            inventario.vender_producto(nombre, cantidad)
        elif opcion == '7':
            print("Saliendo del sistema.")
            exit()
        else:
            print("Opción no válida, por favor intente de nuevo.")


# Inicialización del inventario con los productos
inventario = inicializar_inventario()

# Ejecutar el menú
mostrar_menu(inventario)

