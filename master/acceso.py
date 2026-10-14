from dataclasses import dataclass

from .errores import ErrorDominio
from .prioridad import Prioridad
from .requisito import Requisito
from .titulacion import Titulacion


@dataclass(frozen=True)
class Acceso:
    titulacion: Titulacion
    prioridad: Prioridad
    requisitos: tuple[Requisito, ...] = ()

    def __post_init__(self) -> None:
        if not isinstance(self.titulacion, Titulacion):
            raise ErrorDominio("El acceso necesita una titulación válida.")
        if not isinstance(self.prioridad, Prioridad):
            raise ErrorDominio("El acceso necesita una prioridad válida.")
        if not isinstance(self.requisitos, tuple) or not all(
            isinstance(requisito, Requisito) for requisito in self.requisitos
        ):
            raise ErrorDominio("Los requisitos de acceso deben ser una tupla válida.")
