from datetime import date
from clientes import Cliente
from empleado import Cajero
from medicamento import Medicamento


class Venta:
    def __init__(self, empleado_encargado, metodo_de_pago, fecha, cliente):
        self.empleado_encargado = empleado_encargado
        self.cliente = cliente
        self.metodo_de_pago = metodo_de_pago
        self.fecha = fecha
        self._articulos = []  # aquí se guardara dicccionarios {"medicamento": x, "cantidad": y}

    @property
    def articulos(self):
        return self._articulos

    def agregar_articulos(self, medicamento, cantidad):  # Acumula en self.articulos
        if cantidad > 0:
            medicamento.reducir_stock(cantidad)
            self._articulos.append({"medicamento": medicamento, "cantidad": cantidad})

    def generar_recibo(self):
        print("====================")
        print("Medicamentos:")

        for articulo in self.articulos:
            print(
                f"-- {articulo['medicamento']} x{articulo['cantidad']}\nPrecio: {articulo['medicamento'].precio}"
            )

        print(f"Cliente: {self.cliente.nombre}")
        print(f"Atendido por: {self.empleado_encargado.nombre}")
        print(f"Fecha: {self.fecha}")
        print("Gracias por su compra")
        print("====================")

    def to_dict(self):
        return {
            "empleado_encargado": self.empleado_encargado.to_dict(),
            "cliente": self.cliente.to_dict(),
            "articulos": [
                {
                    "medicamento": objeto["medicamento"].to_dict(),
                    "cantidad": objeto["cantidad"],
                }
                for objeto in self.articulos
            ],
            "fecha": str(self.fecha),
            "metodo_de_pago": self.metodo_de_pago,
        }

    @classmethod
    def desde_dict(cls, datos):
        venta = cls(
            Cajero.desde_dict(datos["empleado_encargado"]),
            datos["metodo_de_pago"],
            date.fromisoformat(datos["fecha"]),
            Cliente.desde_dict(datos["cliente"]),
        )
        for compra in datos["articulos"]:
            venta.agregar_articulos(
                Medicamento.desde_dict(compra["medicamento"]),
                compra["cantidad"],
            )
        return venta
