from datetime import date
from medicamento import Medicamento
from clientes import Cliente

medicamento1 = Medicamento("Ibuprofeno", 2000, 4, date(2027, 1, 1), receta=True)

medicamento2 = Medicamento("Amoxicilina", 3500, 3, date(2026, 8, 20), receta=True)
medicamento3 = Medicamento("Paracetamol", 1200, 50, date(2027, 6, 15))
medicamento4 = Medicamento("Loratadina", 800, 30, date(2028, 3, 10))
medicamento5 = Medicamento("Omeprazol", 1500, 2, date(2027, 11, 5), receta=True)
medicamento6 = Medicamento("Metformina", 2500, 20, date(2027, 4, 18), receta=True)
medicamento7 = Medicamento("Vitamina C", 600, 100, date(2029, 1, 1))
medicamento8 = Medicamento("Aspirina", 900, 45, date(2027, 9, 30))
medicamento9 = Medicamento("Diazepam", 4000, 1, date(2026, 12, 1), receta=True)
medicamento10 = Medicamento("Hidrocortisona", 1800, 8, date(2027, 7, 22))


cliente1 = Cliente("Esteban Mora", 101110111)
cliente2 = Cliente("Laura Jiménez", 205340821)
cliente3 = Cliente("Carlos Vega", 302150934)
cliente4 = Cliente("Sofía Ramírez", 408761245)
cliente5 = Cliente("Andrés Solano", 512390678)


data_medicamentos = [
    medicamento1,
    medicamento2,
    medicamento3,
    medicamento4,
    medicamento5,
    medicamento6,
    medicamento7,
    medicamento8,
    medicamento9,
    medicamento10,
]
data_clientes = [
    cliente1,
    cliente2,
    cliente3,
    cliente4,
    cliente5,
]
