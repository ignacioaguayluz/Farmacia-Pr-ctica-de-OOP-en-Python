from datetime import date, timedelta
from excepciones import StockInsuficienteError

HOY = date.today()
DIAS_A_SUMAR = timedelta(days=90)


class Medicamento:
    def __init__(self, nombre, precio, stock, fecha_venc, receta=False):
        self.nombre = nombre
        self._precio = precio
        self._stock = stock
        self.fecha_venc = fecha_venc
        self.receta = receta

    def __str__(self):
        return f"{self.nombre} tiene un precio de {self._precio}, hay disponibles {self._stock}, vencen: {self.fecha_venc}"

    def esta_disponible(self):  # verifica si el stock es mayor a 0
        if self._stock > 0:
            return f"El {self.nombre} está disponible."
        else:
            return f"Lo lamentos en este momento no contamos con {self.nombre}."

    @classmethod
    def medicamento_generico(cls, nombre):
        return cls(nombre, precio=500, stock=10, fecha_venc=HOY + DIAS_A_SUMAR)

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        if value < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = value

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError("El stock no puede ser negativo")
        self._stock = value

    def reducir_stock(
        self, cantidad
    ):  # descuenta del stock, y validamos que no baje de 0
        if cantidad > self._stock:
            raise StockInsuficienteError(
                f"Lo siento no tenemos esa cantidad de {self.nombre}"
            )
        else:
            self._stock -= cantidad
            return self.stock

    def agregar_stock(
        self, cantidad
    ):  # cuando introducimos un nuevo cargamento de medicinas
        self._stock += cantidad
        return self.stock

    def esta_vencido(self):  # compara la fecha de vencimiento con la actual
        if self.fecha_venc > HOY:
            print(f"El medicamento {self.nombre} sigue vigente")

        else:
            print(f"El medicamento {self.nombre} esta vencido.")

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "fecha_venc": str(self.fecha_venc),
            "receta": self.receta,
        }

    @classmethod
    def desde_dict(cls, datos):
        return cls(
            datos["nombre"],
            datos["precio"],
            datos["stock"],
            date.fromisoformat(datos["fecha_venc"]),
            datos["receta"],
        )
