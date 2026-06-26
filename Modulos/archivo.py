import json
from Modulos.config import RUTA_JSON

# Leemos el archivo JSON y retornamos los datos, si no existe o está vacío retornamos la estructura base
def leer_datos():
    try:
        with open (RUTA_JSON,"r", encoding="utf-8") as l:
            return json.load(l)
    except (FileNotFoundError,json.JSONDecodeError):
        return {"inventario":[],"ventas":[],"ventas_totales":[],"producto_mas_vendido":[],"ganancia":[]}
    
    
# Guardamos el diccionario completo en el archivo JSON sobreescribiendo el estado anterior    
def guardar_datos(datos):
    with open(RUTA_JSON, 'w', encoding ='utf-8') as g:
        json.dump(datos,g,indent=4)
