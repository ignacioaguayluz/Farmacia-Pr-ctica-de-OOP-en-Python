# Farmacia — Práctica de OOP en Python

Aplicación de consola que simula el sistema de gestión de una farmacia, desarrollada como ejercicio práctico para aplicar los principios de la Programación Orientada a Objetos en Python.

---

# Conceptos de OOP aplicados

| Concepto | Dónde se aplica |
|---|---|
| **Clases y objetos** | `Medicamento`, `Cliente`, `Venta`, `Receta`, `Empleado` |
| **Herencia** | `Cajero` y `Farmaceutico` heredan de `Empleado` |
| **Encapsulamiento** | `_stock`, `_precio`, `_historial`, `_articulos` con `@property` y setters |
| **Polimorfismo** | Método `tarea_realiza()` sobreescrito en `Cajero` y `Farmaceutico` |
| **Clases abstractas** | `Empleado` hereda de `ABC` y define `tarea_realiza()` como abstracto |
| **Métodos especiales** | `__str__` en `Medicamento`, `Receta` |
| **`@staticmethod`** | `Receta.validar_fecha()` para verificar vigencia de fechas |
| **`@classmethod`** | `Medicamento.medicamento_generico()` y `desde_dict()` en todas las clases |
| **Excepciones personalizadas** | `StockInsuficienteError`, `RecetaInvalidaError`, `RecetaUtilizadaError`, `ArchivoNoEncontradoError` |
| **Persistencia JSON** | Guardado y carga completa del estado de la farmacia |

---

# Estructura del proyecto

```
farmacia/
├── main.py              # Punto de entrada, simulación del flujo completo
├── farmacia.py          # Clase central que orquesta el sistema
├── medicamento.py       # Clase Medicamento con manejo de stock
├── empleado.py          # Clases Empleado, Cajero y Farmaceutico
├── clientes.py          # Clase Cliente con historial de compras
├── receta.py            # Clase Receta con validación de uso
├── venta.py             # Clase Venta con generación de recibo
├── persistencia.py      # Guardado y carga de datos en JSON
├── excepciones.py       # Excepciones personalizadas del sistema
└── datos.py             # Datos de ejemplo: medicamentos y clientes
```

---

## 🔄 Flujo del sistema

1. La farmacia recibe un lote de medicamentos
2. Un cliente solicita un medicamento
3. Si requiere receta, el **Farmacéutico** la valida
4. El **Cajero** procesa la venta y registra el método de pago
5. El stock se descuenta automáticamente
6. Se genera un recibo con el detalle de la compra
7. La farmacia detecta medicamentos con stock bajo (menos de 5 unidades)
8. El estado completo se guarda y puede cargarse desde un archivo JSON

---

# Cómo correrlo

```bash
python3 main.py
```

---

# Ejemplo de salida

```
====================
Medicamentos:
-- Vitamina C tiene un precio de 600, hay disponibles 98, vencen: 2029-01-01 x2
Precio: 600
Cliente: Sofía Ramírez
Atendido por: Juan Perez
Fecha: 2026-05-01
Gracias por su compra
====================
Hay que reponer más stock de Ibuprofeno
Hay que reponer más stock de Diazepam
```

---

# Requisitos

Python 3.10 o superior. No requiere dependencias externas.