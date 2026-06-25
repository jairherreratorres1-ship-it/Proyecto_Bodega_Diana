from Modulos.archivo import guardar_datos
from Modulos.config import LINEA_SEPARADORA

class Reporte:
    def __init__(self, ventas):
        self.ventas = ventas

    def total_ventas(self):
        return len(self.ventas)

    def producto_mas_vendido(self):
        conteo = {}

        for venta in self.ventas:
            producto = venta["producto"]
            conteo[producto] = conteo.get(producto, 0) + venta["cantidad"]

        if not conteo:
            return "Sin ventas"

        return max(conteo, key=conteo.get)

    def calcular_ingresos(self):
        return sum(venta["total"] for venta in self.ventas)

    def calcular_ganancia(self):
        return self.calcular_ingresos() * 0.10

    def __str__(self):
        return (
            f"Total ventas: {self.total_ventas()}\n"
            f"Producto más vendido: {self.producto_mas_vendido()}\n"
            f"Ingresos totales: {self.calcular_ingresos()}\n"
            f"Ganancia: {self.calcular_ganancia()}"
        )

    def diccionario(self, id_reporte, fecha):
        return {
            "id": id_reporte,
            "fecha": fecha,
            "total_ventas": self.total_ventas(),
            "producto_mas_vendido": self.producto_mas_vendido(),
            "ingresos_totales": self.calcular_ingresos(),
            "ganancia_total": self.calcular_ganancia()
        }
        
def generar_reporte(datos):
    fecha = input("Ingresa la fecha (YYYY-MM-DD): ").strip()

    ventas_filtradas = [venta for venta in datos["ventas"] if venta["fecha_venta"] == fecha]

    reporte = Reporte(ventas_filtradas)
    
    print(LINEA_SEPARADORA)
    print(reporte)
    print(LINEA_SEPARADORA)

    check = input("¿Guardar reporte? SI/NO: ").strip().upper()

    if check == "SI":
        datos["reporte"].append(reporte.diccionario(len(datos["reporte"]) + 1,fecha))
        guardar_datos(datos)
        print("Reporte guardado exitosamente.")
    else:
        print("Operación cancelada.")