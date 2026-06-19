import json
from Database.archivo import leer_datos, guardar_datos
from config import LINEA_SEPARADORA


def agregar_producto():
    datos = leer_datos()
    nuevo_producto = {
        "id": len(datos)+1,
        "producto": input("Ingresa el nombre del producto: "),
        "stock": int(input("Ingresa el la cantidad del producto: ")),
        "precio": float(input("Ingresa el precio del producto: "))
    }
    print(LINEA_SEPARADORA)
    print("producto a agregar\n{nuevo_producto}")
    print(LINEA_SEPARADORA)
    
    check = input("Deseas agregar el producto? SI/NO: ").strip().upper()
    if check == "SI":
        datos.append(nuevo_producto)
        guardar_datos(datos)
        print("Producto guardado exitosamente")
    else:
        print("Operación Cancelada")
        return

def eliminar_producto():
    datos = leer_datos()
    nombre_producto = input("Ingrese el nombre del producto a eliminar: ")
    datos  = [producto for producto in datos if producto[0] != nombre_producto]
    guardar_datos(datos)

def actualizar_producto():
    datos = leer_datos()
    nombre_producto = input("Ingrese el nombre del producto a actualizar: ")
    for i, producto in enumerate(datos):
        if producto[0] == nombre_producto:
            nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: "))
            if nueva_cantidad < 0:
                print("La cantidad no puede ser negativa.")
                return