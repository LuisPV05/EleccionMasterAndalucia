"""Criterios utilizados para valorar la solicitud de un máster."""

from dataclasses import dataclass
from math import isfinite

from .errores import ErrorDominio


@dataclass(frozen=True)
class Criterio:
    """Aspecto de valoración con ponderación opcional si se conoce."""

    nombre: str
    ponderacion: float | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.nombre, str) or not self.nombre.strip():
            raise ErrorDominio("El nombre del criterio no puede estar vacío.")
        if self.ponderacion is not None and (
            isinstance(self.ponderacion, bool)
            or not isinstance(self.ponderacion, (int, float))
            or not isfinite(self.ponderacion)
            or not 0 <= self.ponderacion <= 100
        ):
            raise ErrorDominio("La ponderación debe estar entre 0 y 100.")
