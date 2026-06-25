from Modulos.config import BANNER_BIENVENIDA, LINEA_SEPARADORA
from Modulos.archivo import leer_datos
from Modulos.operacion import agregar_producto, buscar_producto, eliminar_producto, actualizar_producto, mostrar_inventario
from Modulos.Ventas import registrar_venta
from Modulos.reportes import generar_reporte

def mostrar_menu():
    print(BANNER_BIENVENIDA)
    print("1. Buscar Producto")
    print("2. Registrar Venta Directa")
    print("3. Ver Inventario Completo")
    print("4. Gestionar Mercadería (Agregar / Actualizar / Eliminar)")
    print("5. Generar Reporte")
    print("6. Salir")
    print(LINEA_SEPARADORA)

def menu_mercaderia(datos):
    while True:
        print("\n--- GESTIÓN DE MERCADERÍA ---")
        print("1. Agregar Nuevo Producto")
        print("2. Actualizar Stock / Precio de un Producto")
        print("3. Eliminar Producto")
        print("4. Volver al Menú Principal")
        opcion = input("Selecciona una opción: ").strip()
        
        if opcion == "1":
            agregar_producto(datos)
        elif opcion == "2":
            actualizar_producto(datos)
        elif opcion == "3":
            eliminar_producto(datos)
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

def flujo_buscar_y_vender(datos):
    producto_encontrado = buscar_producto(datos)
    
    if producto_encontrado:
        check_venta = input("¿Deseas registrar una venta para este producto? SI/NO: ").strip().upper()
        if check_venta == "SI":
            registrar_venta(datos, producto_encontrado)

def flujo_ver_inventario(datos):
    inventario_tiene_productos = mostrar_inventario(datos)
    
    if inventario_tiene_productos:
        check_actualizar = input("¿Deseas actualizar el stock o precio de algún producto de la lista? SI/NO: ").strip().upper()
        if check_actualizar == "SI":
            actualizar_producto(datos)

def main():
    datos = leer_datos()
    
    inicio = input("¿Desea mostrar el menú de opciones? SI/NO: ").strip().upper()
    if inicio != "SI":
        print("Operación cancelada. Cerrando el sistema.")
        return

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-6): ").strip()
        
        if opcion == "1":
            flujo_buscar_y_vender(datos)
        elif opcion == "2":
            registrar_venta(datos)
        elif opcion == "3":
            flujo_ver_inventario(datos)
        elif opcion == "4":
            menu_mercaderia(datos)
        elif opcion == "5":
            generar_reporte(datos)
        elif opcion == "6":
            print("Saliendo del sistema... ¡Gracias por usar Bodega Diana!")
            break
        else:
            print("Opción inválida.")
        
        regresar = input("\n¿Regresar al menú de opciones? SI/NO: ").strip().upper()
        if regresar != "SI":
            print("Operación cancelada. Saliendo del sistema.")
            break

if __name__ == "__main__":
    main()