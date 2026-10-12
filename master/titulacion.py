
"""Objeto de valor que representa una titulación universitaria."""


from dataclasses import dataclass


@dataclass(frozen=True)
class Titulacion:
    """Identifica una titulación universitaria por su nombre."""

    nombre: str

    def __post_init__(self) -> None:
        if not self.nombre.strip():
            raise ValueError("El nombre de la titulación no puede estar vacío.")
