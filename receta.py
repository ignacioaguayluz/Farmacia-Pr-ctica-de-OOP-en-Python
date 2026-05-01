from excepciones import RecetaUtilizadaError
from datetime import date

from medicamento import Medicamento


class Receta:
    def __init__(self, medicamento, fecha_emision, fecha_venc, medico):
        self.medicamento = medicamento
        self._utilizada = False
        self.fecha_emision = fecha_emision
        self.fecha_venc = fecha_venc
        self.medico = medico

    def __str__(self):
        return (
            f"Medicamento: {self.medicamento}\n"
            f"Fecha de emisión: {self.fecha_emision}\n"
            f"Fecha de vencimiento: {self.fecha_venc}\n"
            f"Medico: {self.medico}\n"
            f"Utilizida: {'Si' if self.utilizada else 'No'}"
        )

    @property
    def utilizada(self):
        return self._utilizada

    @utilizada.setter
    def utilizada(self, value):
        if self._utilizada is True:
            raise RecetaUtilizadaError("No se puede volver a utilizar una receta.")
        self._utilizada = value

    @staticmethod
    def validar_fecha(fecha):
        if fecha > date.today():
            return True
        else:
            return False

    def to_dict(self):
        return {
            "medicamento": self.medicamento.to_dict(),
            "fecha_emision": str(self.fecha_emision),
            "fecha_venc": str(self.fecha_venc),
            "medico": self.medico,
        }

    @classmethod
    def desde_dict(cls, datos):
        return cls(
            Medicamento.desde_dict(datos["medicamento"]),
            date.fromisoformat(datos["fecha_venc"]),
            date.fromisoformat(datos["fecha_emision"]),
            datos["medico"],
        )
