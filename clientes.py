from datetime import date
from medicamento import Medicamento
from receta import Receta


class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self._historial = []

    @property
    def historial(self):
        return self._historial

    def agregar_compra(self, fecha, medicamento, receta):
        compras = {
            "fecha": fecha,
            "medicamento": medicamento,
            "receta": receta,
        }
        self._historial.append(compras)

    def ver_historial(self):
        if not self._historial:
            return "Este cliente, no tiene historial."
        else:
            for compra in self._historial:
                print(f"Fecha: {compra['fecha']}")
                print(f"Medicamento: {compra['medicamento']}")
                print(f"Receta: {compra['receta']}")
                print("-------------------------")

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "cedula": self.cedula,
            "historial": [
                {
                    "fecha": str(objeto["fecha"]),
                    "medicamento": objeto["medicamento"].to_dict(),
                    "receta": objeto["receta"].to_dict(),
                }
                for objeto in self._historial
            ],
        }

    @classmethod
    def desde_dict(cls, datos):
        cliente = cls(datos["nombre"], datos["cedula"])
        for compra in datos["historial"]:
            cliente.agregar_compra(
                date.fromisoformat(compra["fecha"]),
                Medicamento.desde_dict(compra["medicamento"]),
                Receta.desde_dict(compra["receta"]),
            )

        return cliente
