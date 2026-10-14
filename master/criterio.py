from dataclasses import dataclass
from decimal import Decimal

from .errores import ErrorDominio


@dataclass(frozen=True)
class Criterio:
    nombre: str
    ponderacion: Decimal
    calculable: bool

    def __post_init__(self) -> None:
        if not isinstance(self.nombre, str) or not self.nombre.strip():
            raise ErrorDominio("El nombre del criterio no puede estar vacío.")
        if not isinstance(self.ponderacion, Decimal):
            raise ErrorDominio("La ponderación debe ser Decimal.")
        if not Decimal("0") <= self.ponderacion <= Decimal("100"):
            raise ErrorDominio("La ponderación debe estar entre 0 y 100.")
        if not isinstance(self.calculable, bool):
            raise ErrorDominio("La calculabilidad debe ser booleana.")
        object.__setattr__(self, "nombre", self.nombre.strip())