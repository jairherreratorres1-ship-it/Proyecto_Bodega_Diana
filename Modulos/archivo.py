import json
from Modulos.config import RUTA_JSON


def leer_datos():
    try:
        with open (RUTA_JSON,"r", encoding="utf-8") as l:
            return json.load(l)
    except (FileNotFoundError,json.JSONDecodeError):
        return {"inventario":[],"ventas":[],"reporte":[]}
    
def guardar_datos(datos):
    with open(RUTA_JSON, 'w', encoding ='utf-8') as g:
        json.dump(datos,g,indent=4)
