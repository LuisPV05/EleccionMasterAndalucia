from dataclasses import dataclass

from .corte import Corte
from .errores import ErrorDominio


@dataclass(frozen=True)
class Adjudicacion:
    convocatoria: str
    codigo_master: str
    corte: Corte

    def __post_init__(self) -> None:
        if not isinstance(self.convocatoria, str):
            raise ErrorDominio("La convocatoria debe ser texto.")
        convocatoria = self.convocatoria.strip()
        if not convocatoria:
            raise ErrorDominio("La convocatoria de una adjudicación no puede estar vacía.")
        if not isinstance(self.codigo_master, str) or len(self.codigo_master) != 6 or not self.codigo_master.isdigit():
            raise ErrorDominio("El código del máster debe contener seis cifras.")
        if not isinstance(self.corte, Corte):
            raise ErrorDominio("La adjudicación necesita un corte válido.")
        object.__setattr__(self, "convocatoria", convocatoria)