import json
from Modulos.archivo import guardar_datos
from Modulos.config import LINEA_SEPARADORA


def buscar_producto(datos):
    nProducto = input("Ingresa el nombre del producto: ").strip().upper()
    
    for producto in datos["inventario"]:
        if producto["producto"].upper() == nProducto:
            print(LINEA_SEPARADORA)
            print(f'Producto encontrado:\nID: {producto["id"]}\nProducto: {producto["producto"]}\nStock: {producto["stock"]}\nPrecio: {producto["precio"]}')
            print(LINEA_SEPARADORA)
            return producto
    else:
        print("Producto no encontrado.")
        return None


def agregar_producto(datos):
    nuevo_id = len(datos["inventario"])+1
    nuevo_producto = input("Ingresa el nombre del producto: ").strip().upper()
    nuevo_stock = int(input("Ingresa el la cantidad del producto: "))
    nuevo_precio=  float(input("Ingresa el precio del producto: "))
    
    productoAgregado = {
        "id": nuevo_id,
        "producto": nuevo_producto,
        "stock":nuevo_stock,
        "precio": nuevo_precio
    }
    
    print(LINEA_SEPARADORA)
    print(f'DATOS DEL NUEVO PRODUCTO:\nProducto: {nuevo_producto}\nStock: {nuevo_stock}\nPrecio: {nuevo_precio}')
    print(LINEA_SEPARADORA)
    
    check = input("Deseas agregar el producto? SI/NO: ").strip().upper()
    if check == "SI":
        datos["inventario"].append(productoAgregado)
        guardar_datos(datos)
        print("Producto guardado exitosamente")
    else:
        print("Operación Cancelada.")
        
        
def eliminar_producto(datos):
    nombre_producto = input("Ingrese el nombre del producto a eliminar: ").strip().upper()
    
    for producto in datos["inventario"]:
        if producto["producto"].upper() == nombre_producto:
            print(LINEA_SEPARADORA)
            print(f"El nombre de producto es: {producto["producto"]}\nStock Actual: {producto["stock"]}\nPrecio Actual: {producto["precio"]}")
            print(LINEA_SEPARADORA)
            
            check = input("Deseas eliminar el producto? SI/NO").strip().upper()
            
            if check == "SI":
                datos["inventario"].remove(producto)
                guardar_datos(datos)
                print("Producto eliminado.")
            else:
                print("Operación cancelada.")
            return
    else:
        print("Producto no encontrado.")
        
            
        

def actualizar_producto(datos):
    nombre_producto = input("Ingrese el nombre del producto a actualizar: ").strip().upper()
    for producto in datos["inventario"]:
        if producto["producto"].upper() == nombre_producto:
            print(LINEA_SEPARADORA)
            print(f"El nombre de producto es: {producto["producto"]}\nStock Actual: {producto["stock"]}\nPrecio Actual: {producto["precio"]}")
            print(LINEA_SEPARADORA)
            
            while True:
                print("Que deseas modificar?")
                print("1. Modifcar Stock")
                print("2. Modificar Precio")
                print("3. Modificar ambos")
                print("4. Salir")
                opcion = input("Selecciona una opción: ").strip()
                
                if opcion in {"1","2","3","4"}:
                    break
                else:
                    print("Opción invalida, intenta de nuevo.")
                    
            if opcion == "1":
                nuevo_stock = int(input("Ingresa la cantidad: "))
                print(f'Nuevo Stock: {nuevo_stock}')
            elif opcion == "2":
                nuevo_precio = float(input("Ingresa el nuevo precio: "))
                print(f'Nuevo Precio: {nuevo_precio}')
            elif opcion == "3":
                nuevo_stock = int(input("Ingresa la cantidad: "))
                nuevo_precio = float(input("Ingresa el nuevo precio: "))
                print(f'Nuevo Stock: {nuevo_stock}')
                print(f'Nuevo Precio: {nuevo_precio}')
            elif opcion == "4":
                print("Operación Cancelada.")
                return
            
            check = input("Deseas actualizar? Si/No: ").strip().upper()
            
            if check == "SI":
                if opcion == "1":
                    producto["stock"] = nuevo_stock
                elif opcion == "2":
                    producto["precio"] = nuevo_precio
                elif opcion == "3":
                    producto["stock"] = nuevo_stock
                    producto["precio"] = nuevo_precio
                guardar_datos(datos)
                print("Datos actualizados correctamente")
            else:
                print("Operación cancelada.")
            return
    else:
        print("Producto no encontrado.")
        
def mostrar_inventario(datos):
    
    print(LINEA_SEPARADORA)
    if not datos["inventario"]:
        print("El inventario está vacío.")
        print(LINEA_SEPARADORA)
        return False
        
    print("               INVENTARIO ACTUAL")
    print(LINEA_SEPARADORA)
    for p in datos["inventario"]:
        print(f"ID: {p['id']} | Producto: {p['producto']} | Stock: {p['stock']} | Precio: S/.{p['precio']:.2f}")
    print(LINEA_SEPARADORA)
    return True