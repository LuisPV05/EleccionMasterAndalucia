from dataclasses import dataclass
from decimal import Decimal
from enum import Enum

from .prioridad_carreras import PrioridadCarrera

class EstadoCorte(Enum):
    TODOS_ADMITIDOS = "TODOS_ADMITIDOS"
    SIN_ADJUDICACION = "SIN_ADJUDICACION"

@dataclass(frozen=True)
class CorteNumerico:
    prioridad: PrioridadCarrera
    puntuacion: Decimal

    def __post_init__(self) -> None:
        if not isinstance(self.prioridad, PrioridadCarrera):
            raise ValueError("El corte numérico necesita una prioridad de carrera válida.")
        if not isinstance(self.puntuacion, Decimal) or self.puntuacion < Decimal("0"):
            raise ValueError("La puntuación de corte debe ser Decimal no negativa.")
