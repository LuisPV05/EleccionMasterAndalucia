"""Objeto de valor que representa la nota media de un expediente."""

from dataclasses import dataclass
from math import isfinite

from .errores import ErrorDominio


@dataclass(frozen=True)
class NotaMedia:
    """Nota media del expediente académico de una estudiante."""

    valor: float

    def __post_init__(self) -> None:
        if isinstance(self.valor, bool) or not isinstance(self.valor, (int, float)):
            raise ErrorDominio("La nota media debe ser numérica.")
        if not isfinite(self.valor):
            raise ErrorDominio("La nota media debe ser un número finito.")
        if not 0 <= self.valor <= 10:
            raise ErrorDominio("La nota media debe estar entre 0 y 10.")
