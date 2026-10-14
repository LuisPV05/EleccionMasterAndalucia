from dataclasses import dataclass
from decimal import Decimal

from .errores import ErrorDominio


@dataclass(frozen=True)
class NotaMedia:
    valor: Decimal

    def __post_init__(self) -> None:
        if not isinstance(self.valor, Decimal):
            raise ErrorDominio("La nota media debe ser Decimal.")
        if not Decimal("0") <= self.valor <= Decimal("10"):
            raise ErrorDominio("La nota media debe estar entre 0 y 10.")