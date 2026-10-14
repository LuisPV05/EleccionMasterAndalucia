from dataclasses import dataclass

from .errores import ErrorDominio


@dataclass(frozen=True)
class Requisito:
    descripcion: str
    obligatorio: bool = True

    def __post_init__(self) -> None:
        if not isinstance(self.descripcion, str) or not self.descripcion.strip():
            raise ErrorDominio("La descripción del requisito no puede estar vacía.")
        if not isinstance(self.obligatorio, bool):
            raise ErrorDominio("El carácter obligatorio debe ser verdadero o falso.")
        object.__setattr__(self, "descripcion", self.descripcion.strip())