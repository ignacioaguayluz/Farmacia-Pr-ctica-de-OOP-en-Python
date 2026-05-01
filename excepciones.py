class FarmaciaError(Exception):
    pass


class RecetaUtilizadaError(FarmaciaError):
    pass


class StockInsuficienteError(FarmaciaError):
    pass


class RecetaInvalidaError(FarmaciaError):
    pass


class MedicamentoNoEncontrado(FarmaciaError):
    pass


class ArchivoNoEncontradoError(FarmaciaError):
    pass
