
"""Objeto de valor que representa una puntuación de admisión."""


from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True)
class Puntuacion:
    """Representa una puntuación numérica obtenida en una valoración."""

    valor: float

    def __post_init__(self) -> None:
        if not isfinite(self.valor):
            raise ValueError("La puntuación debe ser un número finito.")
        if self.valor < 0:
            raise ValueError("La puntuación no puede ser negativa.")
