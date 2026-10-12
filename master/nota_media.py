
"""Objeto de valor que representa la nota media de un expediente."""


from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True)
class NotaMedia:
    """Nota media del expediente académico de una estudiante."""

    valor: float

    def __post_init__(self) -> None:
        if not isfinite(self.valor):
            raise ValueError("La nota media debe ser un número finito.")
        if not 0 <= self.valor <= 10:
            raise ValueError("La nota media debe estar entre 0 y 10.")
