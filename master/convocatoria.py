from collections.abc import Mapping
from dataclasses import dataclass

from .errores import ErrorDominio
from .master import Master

@dataclass(frozen=True)
class Convocatoria:
    identificador: str
    masters: Mapping[str, Master]

    def __post_init__(self) -> None:
        if not isinstance(self.identificador, str) or not self.identificador.strip():
            raise ErrorDominio("El identificador de convocatoria debe ser texto no vacío.")
        if not isinstance(self.masters, Mapping):
            raise ErrorDominio("Los másteres deben estar indexados por código.")
        for codigo, master in self.masters.items():
            if not isinstance(codigo, str) or not codigo.isdigit() or len(codigo) != 6:
                raise ErrorDominio("El código del máster debe contener seis cifras.")
            if not isinstance(master, Master):
                raise ErrorDominio("La convocatoria solo puede contener másteres válidos.")
