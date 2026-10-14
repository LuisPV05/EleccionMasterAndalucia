from dataclasses import dataclass
from decimal import Decimal
from .errores import ErrorDominio
from .prioridad import Prioridad


@dataclass(frozen=True)
class CorteNumerico:
    prioridad: Prioridad
    puntuacion: Decimal

    def __post_init__(self) -> None:
        if not isinstance(self.prioridad, Prioridad):
            raise ErrorDominio("El corte numérico necesita una prioridad válida.")
        if not isinstance(self.puntuacion, Decimal) or self.puntuacion < Decimal("0"):
            raise ErrorDominio("La puntuación de corte debe ser Decimal no negativa.")


@dataclass(frozen=True)
class TodosAdmitidos:
    prioridad: Prioridad = Prioridad.RESTO

    def __post_init__(self) -> None:
        if self.prioridad is not Prioridad.RESTO:
            raise ErrorDominio("El corte especial ** 0,01 debe asociarse a RESTO.")


@dataclass(frozen=True)
class SinAdjudicacion:
    pass


Corte = CorteNumerico | TodosAdmitidos | SinAdjudicacion
