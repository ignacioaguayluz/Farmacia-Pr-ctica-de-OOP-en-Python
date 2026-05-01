import json
from datetime import datetime

from farmacia import Farmacia
from venta import Venta
from excepciones import ArchivoNoEncontradoError


class Persistencia:
    def __init__(self, archivo="farmacia.json") -> None:
        self.archivo = archivo

    def guardar_datos(self, farmacia):
        datos = {
            "nombre": farmacia.nombre,
            "empleados": [empleado.to_dict() for empleado in farmacia.empleados],
            "recetas": [receta.to_dict() for receta in farmacia.recetas],
            "ventas": [venta.to_dict() for venta in farmacia.ventas],
            "fecha_guardado": datetime.now().isoformat(),
        }

        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

    def cargar_datos(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
        except FileNotFoundError:
            raise ArchivoNoEncontradoError("El archivo no existe.")

        farmacia = Farmacia(datos["nombre"])
        for dato_venta in datos["ventas"]:
            venta = Venta.desde_dict(dato_venta)

            farmacia.agregar_ventas(venta)

        return farmacia
