from collections.abc import Mapping
from dataclasses import dataclass

from .master import Master

@dataclass(eq=False)
class ConvocatoriaMaster:
    identificador: str
    masters: Mapping[str, Master]

    def __post_init__(self) -> None:
        if not isinstance(self.identificador, str) or not self.identificador.strip():
            raise ValueError("El identificador de la convocatoria de máster debe ser texto no vacío")
        if not isinstance(self.masters, Mapping):
            raise ValueError("Los másteres deben estar indexados por código.")
        for codigo, master in self.masters.items():
            if not isinstance(codigo, str) or not codigo.isdigit() or len(codigo) != 6:
                raise ValueError("El código del máster debe contener seis cifras.")
            if not isinstance(master, Master):
                raise ValueError("La convocatoria de máster solo puede contener másteres válidos.")
