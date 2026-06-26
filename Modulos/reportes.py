from Modulos.archivo import guardar_datos
from Modulos.config import LINEA_SEPARADORA


# Clase que encapsula las operaciones de análisis sobre las ventas filtradas por fecha
class Reporte:
    # Inicializamos el objeto con la lista de ventas ya filtradas por fecha
    def __init__(self, ventas):
        self.ventas = ventas

    # Contamos el total de transacciones en el período consultado
    def total_ventas(self):
        return len(self.ventas)

    # Identificamos el producto con mayor cantidad vendida en el período
    def producto_con_mayor_venta(self):
        conteo = {}
        for venta in self.ventas:
            producto = venta["producto"]
            conteo[producto] = conteo.get(producto, 0) + venta["cantidad"]
        return max(conteo, key=conteo.get) if conteo else "Sin ventas"

    # Sumamos todos los totales de las ventas filtradas para obtener los ingresos del período
    def calcular_ingresos(self):
        return sum(venta["total"] for venta in self.ventas)

    # Calculamos la ganancia estimada aplicando el 10% sobre los ingresos totales
    def calcular_ganancia(self):
        return self.calcular_ingresos() * 0.10

    # Construimos el diccionario de reporte de cantidad de ventas para guardar en el JSON
    def ventas_totales(self, id_reporte, fecha):
        return {
            "id": id_reporte,
            "fecha": fecha,
            "total_ventas": self.total_ventas()
        }

    # Construimos el diccionario de reporte del producto más vendido para guardar en el JSON
    def producto_mas_vendido(self, id_reporte, fecha):
        return {
            "id": id_reporte,
            "fecha": fecha,
            "producto_mas_vendido": self.producto_con_mayor_venta()
        }

    # Construimos el diccionario de reporte de ingresos y ganancia para guardar en el JSON
    def ganancia(self, id_reporte, fecha):
        return {
            "id": id_reporte,
            "fecha": fecha,
            "ingresos_totales": round(self.calcular_ingresos(),2),
            "ganancia_total": round(self.calcular_ganancia(),2)
        }


# Solicitamos la fecha, filtramos las ventas y mostramos el menú de tipos de reporte disponibles        
def menu_reportes(datos):
    fecha = input("Ingresa la fecha a consultar (YYYY-MM-DD): ").strip()
    ventas_filtradas = [v for v in datos["ventas"] if v["fecha_venta"] == fecha]
    
    reporte_objeto = Reporte(ventas_filtradas)

    while True:
        print(LINEA_SEPARADORA)
        print(f"REPORTES ({fecha})")
        print("1. Reporte de Cantidad de Ventas")
        print("2. Reporte de Producto Más Vendido")
        print("3. Reporte (Ingresos/Ganancias)")
        print("4. Volver al menú principal")
        opcion = input("Selecciona una opción: ").strip()
        
        lista_destino = None
        nuevo_reporte = None
        
        if opcion == "1":
            lista_destino = datos["ventas_totales"]
            nuevo_reporte = reporte_objeto.ventas_totales(len(lista_destino) + 1, fecha)
            
        elif opcion == "2":
            lista_destino = datos["producto_mas_vendidos"]
            nuevo_reporte = reporte_objeto.producto_mas_vendido(len(lista_destino) + 1, fecha)
            
        elif opcion == "3":
            lista_destino = datos["ganancia"]
            nuevo_reporte = reporte_objeto.ganancia(len(lista_destino) + 1, fecha)
            
        elif opcion == "4":
            break
            
        else:
            print("Opción inválida.")
            continue 

        if nuevo_reporte is not None:
            print(LINEA_SEPARADORA)
            print(f'DATOS DEL REPORTE GENERADO: {nuevo_reporte}') 
            print(LINEA_SEPARADORA)
            
            check = input("¿Deseas registrar este reporte? SI/NO: ").strip().upper()
            if check == "SI":
                lista_destino.append(nuevo_reporte)
                guardar_datos(datos)
                print("Reporte registrado exitosamente.")
            else:
                print("Operación cancelada. El reporte no fue guardado.")