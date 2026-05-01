from datetime import date
from farmacia import Farmacia
from clientes import Cliente
from empleado import Cajero, Farmaceutico
from medicamento import Medicamento
from receta import Receta
from venta import Venta
from excepciones import (
    RecetaInvalidaError,
    StockInsuficienteError,
    ArchivoNoEncontradoError,
)
from datos import data_medicamentos, data_clientes
from persistencia import Persistencia


HOY = date.today()

farmacia = Farmacia("Nacho's Drugstore")

cajero = Cajero(2, 20000, "dia", "Juan Perez")
farmaceutico = Farmaceutico(3, 42000, "noche", "María Perez", "F-56378")
cliente = data_clientes
for medicamento in data_medicamentos:
    farmacia.agregar_medicamentos(medicamento)

medicamentos = data_medicamentos
receta = Receta(medicamentos[1], HOY, date(2027, 8, 24), "Pedro Mora")

try:
    farmaceutico.validar_receta(receta)
except RecetaInvalidaError as e:
    print(e)


venta = Venta(cajero, "efectivo", HOY, cliente[3])

cajero.procesar_venta(venta, "efectivo")

cliente[3].agregar_compra(HOY, medicamentos[2], receta)
farmacia.agregar_ventas(venta)
try:
    venta.agregar_articulos(medicamentos[1], 6)
except StockInsuficienteError as e:
    print(e)
try:
    venta.agregar_articulos(medicamentos[6], 2)
except StockInsuficienteError as e:
    print(e)

venta.generar_recibo()
farmacia.stock()
persistencia = Persistencia()
persistencia.guardar_datos(farmacia)

try:
    farmacia_cargada = persistencia.cargar_datos()

    for venta in farmacia_cargada.ventas:
        venta.generar_recibo()
except ArchivoNoEncontradoError as e:
    print(e)
