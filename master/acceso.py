"""Relación de acceso entre una titulación y un máster."""

from dataclasses import dataclass

from .errores import ErrorDominio
from .prioridad import Prioridad
from .requisito import Requisito
from .titulacion import Titulacion


@dataclass(frozen=True)
class Acceso:
    """Prioridad y requisito aplicables a una titulación en un máster."""

    titulacion: Titulacion
    prioridad: Prioridad
    requisito: Requisito | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.titulacion, Titulacion):
            raise ErrorDominio("El acceso necesita una titulación válida.")
        if not isinstance(self.prioridad, Prioridad):
            raise ErrorDominio("El acceso necesita una prioridad válida.")
        if self.requisito is not None and not isinstance(self.requisito, Requisito):
            raise ErrorDominio("El requisito de acceso no tiene un tipo válido.")