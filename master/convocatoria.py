from collections.abc import Mapping

from .master import Master

class Convocatoria:
    def __init__(self, identificador: str, masters: Mapping[str, Master]) -> None:
        if not isinstance(identificador, str) or not identificador.strip():
            raise ValueError("El identificador de convocatoria debe ser texto no vacío.")
        if not isinstance(masters, Mapping):
            raise ValueError("Los másteres deben estar indexados por código.")
        for codigo, master in masters.items():
            if not isinstance(codigo, str) or not codigo.isdigit() or len(codigo) != 6:
                raise ValueError("El código del máster debe contener seis cifras.")
            if not isinstance(master, Master):
                raise ValueError("La convocatoria solo puede contener másteres válidos.")
        self._identificador = identificador
        self._masters = masters
