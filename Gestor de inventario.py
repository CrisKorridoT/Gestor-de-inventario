class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad):
        self.stock += cantidad

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def generar_informe(self):
        print("Informe de inventario:")
        for producto in self.productos:
            print(producto)

    def vender_producto(self, codigo, cantidad):
        producto = self.buscar_producto(codigo)
        if producto:
            if producto.stock >= cantidad:
                producto.actualizar_stock(-cantidad)
                return Venta(producto, cantidad)
            else:
                print("Stock insuficiente para realizar la venta.")
        else:
            print("Producto no encontrado en el inventario.")
          
    def actualizar_producto(self, codigo, nuevo_nombre, nuevo_precio, nuevo_stock):
        producto = self.buscar_producto(codigo)
        if producto:
            producto.nombre = nuevo_nombre
            producto.precio = nuevo_precio
            producto.stock = nuevo_stock
            print(f"Producto {codigo} actualizado:")
            print(producto)
        else:
            print("Producto no encontrado en el inventario.")      


class Venta:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
        self.total = producto.precio * cantidad

    def __str__(self):
        return f"Venta - Producto: {self.producto.nombre}, Cantidad: {self.cantidad}, Total: {self.total}"


# Ejemplo de uso del sistema
inventario = Inventario()

# Agregar productos al inventario
producto1 = Producto("P1", "Camiseta", 15.99, 50)
producto2 = Producto("P2", "Pantalón", 29.99, 30)

inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)

# Generar informe de inventario
inventario.generar_informe()

# Actualizar los datos de un producto existente
inventario.actualizar_producto("P1", "Camiseta de manga corta", 17.99, 40)

# Realizar una venta
venta1 = inventario.vender_producto("P1", 5)
if venta1:
    print(venta1)

# Generar informe de inventario
inventario.generar_informe()