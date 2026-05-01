from datetime import date
from abc import ABC, abstractmethod
from typing import Protocol
from excepciones import RecetaInvalidaError
from receta import Receta


HOY = date.today()


class RealizandoProtocol(Protocol):
    def tarea_realiza(self) -> None | str:
        """Comprueba que función esta cumpliendo el empleado."""
        ...


class Empleado(ABC):
    def __init__(self, id_empleado: int, salario: int, turno: str, nombre: str) -> None:
        self.id_empleado = id_empleado
        self._salario = salario
        self.turno = turno
        self.nombre = nombre

    def tarea_realiza(self):
        return "El empleado esta realizando su tarea."

    def validacion_turno(self):
        if self.turno == "noche":
            return f"{self.nombre} ID: {self.id_empleado} se encuentra en el turno de noche."
        elif self.turno == "dia":
            return (
                f"{self.nombre} ID: {self.id_empleado} se encuentra en el turno de día."
            )
        elif self.turno == "tarde":
            return f"{self.nombre} ID: {self.id_empleado} se encuentra en el turno de la tarde."

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, value):
        if value <= 0:
            raise ValueError("El salario no puede ser 0 ni negativo.")
        self._salario = value

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "id": self.id_empleado,
            "salario": self.salario,
            "turno": self.turno,
        }


class Cajero(Empleado):
    def __init__(self, id_empleado, salario, turno, nombre):
        super().__init__(id_empleado, salario, turno, nombre)

    def procesar_venta(self, venta, metodo_de_pago):

        if metodo_de_pago == "efectivo" or metodo_de_pago == "tarjeta":
            venta.metodo_de_pago = metodo_de_pago
            return venta.metodo_de_pago
        else:
            return f"El método de pago {metodo_de_pago} no es válido."

    def tarea_realiza(self):
        return f"{self.nombre} esta realizando su tarea como cajero."

    @classmethod
    def desde_dict(cls, datos):
        return cls(
            datos["id"],
            datos["salario"],
            datos["turno"],
            datos["nombre"],
        )


class Farmaceutico(Empleado):
    def __init__(
        self, id_empleado, salario, turno, nombre, licencia_medica: str
    ) -> None:
        super().__init__(id_empleado, salario, turno, nombre)
        self.licencia_medica = licencia_medica

    def validar_receta(self, receta):
        if not Receta.validar_fecha(receta.fecha_venc) or receta.utilizada == True:
            raise RecetaInvalidaError("Receta no valida.")
        else:
            return receta

    def tarea_realiza(self):
        return f"{self.nombre} esta realizando su tarea como farmacéutico."
