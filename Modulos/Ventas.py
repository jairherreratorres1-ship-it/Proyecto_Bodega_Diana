from datetime import date
from Modulos.config import LINEA_SEPARADORA
from Modulos.operacion import buscar_producto
from Modulos.archivo import guardar_datos

class Venta:
    def __init__(self, producto, cantidad):
        self.id_producto = producto["id"]
        self.producto = producto["producto"]
        self.precio_unitario = producto["precio"]
        self.cantidad = cantidad
    
    def seleccionar_metodo_pago(self):
        
        metodos = {
            "1": "Efectivo",
            "2": "Tarjeta",
            "3": "Yape / Plin",
        }
        while True:
            print("Cuale es el metodo de pago?")
            print("1. Efectivo")
            print("2. Tarjeta")
            print("3. Yape / Plin")
            print("4. Salir")
            opcion = (input("Selecciona el metodo de pago: ")).strip()
            
            if opcion in ("1","2","3","4"):
                break
            else:
                print("Opción ingresada no es valida, intente nuevamente.")
                
        if opcion == "4":
            return None
        return metodos[opcion]
    
    def ingresar_vendedor(self):
        return input("Ingresa el nombre del vendedor: ").strip().upper()
            
    def calcular_total(self):
        return self.precio_unitario * self.cantidad
    
    def diccionario(self, id_venta):
        return {
            "id": id_venta,
            "id_producto": self.id_producto,
            "producto": self.producto,
            "cantidad": self.cantidad,
            "precio_unitario": round(self.precio_unitario,2),
            "total": self.calcular_total(),
            "metodo_pago": self.seleccionar_metodo_pago(),
            "vendedor": self.ingresar_vendedor(),
            "fecha_venta": str(date.today())
        }
    def __str__(self):
        return f'Producto: {self.producto}\nCantidad: {self.cantidad}\nPrecio unitario: {self.precio_unitario}\nTotal: {self.calcular_total()}'
        
def registrar_venta(datos, producto_encontrado=None):
    if producto_encontrado is None:
        producto_encontrado = buscar_producto(datos)
    
    if producto_encontrado is None:
        return
    
    while True:
        try:
            cantidad = int(input("Ingresa la cantidad a vender: "))
            if cantidad <= 0:
                print("El numero ingresado debe ser mayor a 0")
            else:
                break
        except ValueError:
            print("Error, debe ingresar un número")
    
    if cantidad > producto_encontrado["stock"]:
        print(f'Stock insuficiente. Stock disponible: {producto_encontrado["stock"]}')
        return
    
    venta = Venta(producto_encontrado, cantidad)
    

    print(LINEA_SEPARADORA)
    print(venta)
    print(LINEA_SEPARADORA)
    
    check = input("Confirmar venta? SI/NO: ").strip().upper()
    
    if check == "SI":
        producto_encontrado["stock"] -= cantidad
        datos["ventas"].append(venta.diccionario(len(datos["ventas"]) + 1))
        guardar_datos(datos)
        print("Venta registrada exitosamente.")
    else:
        print("Operación cancelada.")