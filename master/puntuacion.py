from dataclasses import dataclass
from decimal import Decimal

from .errores import ErrorDominio


@dataclass(frozen=True)
class Puntuacion:
    valor: Decimal

    def __post_init__(self) -> None:
        if not isinstance(self.valor, Decimal):
            raise ErrorDominio("La puntuación debe ser Decimal.")
        if self.valor < Decimal("0"):
            raise ErrorDominio("La puntuación no puede ser negativa.")