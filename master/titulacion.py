from dataclasses import dataclass

from .errores import ErrorDominio


@dataclass(frozen=True)
class Titulacion:
    nombre: str

    def __post_init__(self) -> None:
        if not isinstance(self.nombre, str) or not self.nombre.strip():
            raise ErrorDominio("El nombre de la titulación no puede estar vacío.")
        object.__setattr__(self, "nombre", self.nombre.strip())