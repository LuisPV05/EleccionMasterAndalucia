
"""Criterios utilizados para valorar la solicitud de un máster."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Criterio:
    """Representa un criterio de valoración de un máster."""

    nombre: str
    ponderacion: float | None = None

    def __post_init__(self) -> None:
        if not self.nombre.strip():
            raise ValueError("El nombre del criterio no puede estar vacío.")

        if self.ponderacion is not None and not 0 <= self.ponderacion <= 100:
            raise ValueError("La ponderación debe estar entre 0 y 100.")
