"""Objeto de valor que representa una titulación universitaria."""

from dataclasses import dataclass

from .errores import ErrorDominio


@dataclass(frozen=True)
class Titulacion:
    """Titulación universitaria identificada por su denominación."""

    nombre: str

    def __post_init__(self) -> None:
        if not isinstance(self.nombre, str) or not self.nombre.strip():
            raise ErrorDominio("El nombre de la titulación no puede estar vacío.")
