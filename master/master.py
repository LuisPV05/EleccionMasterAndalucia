
"""Máster ofertado en una convocatoria de admisión."""

from dataclasses import dataclass

from .prioridad import Prioridad
from .requisito import Requisito
from .titulacion import Titulacion


@dataclass(frozen=True)
class Master:
    """Representa un máster y sus condiciones de acceso."""

    codigo: str
    nombre: str
    titulacion: Titulacion
    prioridad: Prioridad
    requisito: Requisito | None = None

    def __post_init__(self) -> None:
        if not self.codigo.strip():
            raise ValueError("El código del máster no puede estar vacío.")
        if not self.nombre.strip():
            raise ValueError("El nombre del máster no puede estar vacío.")
