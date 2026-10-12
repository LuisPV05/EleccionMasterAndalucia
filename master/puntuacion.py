"""Objeto de valor que representa una puntuación de admisión."""

from dataclasses import dataclass
from math import isfinite

from .errores import ErrorDominio


@dataclass(frozen=True)
class Puntuacion:
    """Puntuación numérica obtenida en el sistema de valoración de un máster."""

    valor: float

    def __post_init__(self) -> None:
        if isinstance(self.valor, bool) or not isinstance(self.valor, (int, float)):
            raise ErrorDominio("La puntuación debe ser numérica.")
        if not isfinite(self.valor):
            raise ErrorDominio("La puntuación debe ser un número finito.")
        if self.valor < 0:
            raise ErrorDominio("La puntuación no puede ser negativa.")
