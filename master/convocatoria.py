from collections.abc import Mapping
from dataclasses import dataclass
from types import MappingProxyType
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
        masters = dict(self.masters)
        for codigo, master in masters.items():
            if not isinstance(master, Master):
                raise ErrorDominio("La convocatoria solo puede contener másteres válidos.")
            if codigo != master.codigo or master.convocatoria != self.identificador.strip():
                raise ErrorDominio("El código y la convocatoria deben coincidir con el máster.")
        object.__setattr__(self, "identificador", self.identificador.strip())
        object.__setattr__(self, "masters", MappingProxyType(masters))
