
"""Requisitos adicionales para acceder a un máster."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Requisito:
    """Representa un requisito adicional asociado a un máster."""

    descripcion: str

    def __post_init__(self) -> None:
        if not self.descripcion.strip():
            raise ValueError("La descripción del requisito no puede estar vacía.")
