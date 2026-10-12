"""Requisitos adicionales para acceder a un máster."""

from dataclasses import dataclass

from .errores import ErrorDominio


@dataclass(frozen=True)
class Requisito:
    """Condición adicional descrita en la ficha de un máster."""

    descripcion: str
    obligatorio: bool

    def __post_init__(self) -> None:
        if not isinstance(self.descripcion, str) or not self.descripcion.strip():
            raise ErrorDominio("La descripción del requisito no puede estar vacía.")
        if not isinstance(self.obligatorio, bool):
            raise ErrorDominio("El carácter obligatorio debe ser verdadero o falso.")
