from medicamento import Medicamento
from empleado import Cajero, Farmaceutico
from receta import Receta
from venta import Venta
from excepciones import MedicamentoNoEncontrado


class Farmacia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.medicamentos = []
        self.empleados = []
        self.recetas = []
        self.ventas = []

    def __str__(self):
        return f"¡Bienvenido a la farmacia {self.nombre}!"

    def agregar_empleados(self, empleado):
        if isinstance(empleado, (Cajero, Farmaceutico)):
            self.empleados.append(empleado)

        else:
            return f"{empleado} no es un puesto válido en esta farmacia."

    def ver_empleados(self):
        for empleado in self.empleados:
            print(empleado)

    def agregar_medicamentos(self, medicamento):
        if isinstance(medicamento, Medicamento):
            self.medicamentos.append(medicamento)
        else:
            return f"{medicamento} no es un medicamento que tengamos."

    def ver_medicamentos(self):
        for medicamento in self.medicamentos:
            print(medicamento)

    def buscar_medicamentos(self, nombre):
        for medicina in self.medicamentos:
            if medicina.nombre == nombre:
                return medicina
        raise MedicamentoNoEncontrado(f"El medicamento {nombre} no fue encontrado.")

    def agregar_recetas(self, receta):
        if isinstance(receta, Receta):
            self.recetas.append(receta)

    def ver_recetas(self):
        for receta in self.recetas:
            print(receta)

    def agregar_ventas(self, venta):
        if isinstance(venta, Venta):
            self.ventas.append(venta)

    def ver_ventas(self):
        for venta in self.ventas:
            print(venta)

    def stock(self):
        limite = 6

        for medicamento in self.medicamentos:
            if medicamento.stock < limite:
                print(f"Hay que reponer más stock de {medicamento.nombre}")
