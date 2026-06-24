import json
import os
from Modulos.archivo import leer_datos,guardar_datos
from Modulos.operacion import agregar_producto,buscar_producto
from Modulos.config import LINEA_SEPARADORA



datos = leer_datos()
buscar_producto(datos)
agregar_producto(datos)