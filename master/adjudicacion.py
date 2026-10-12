
"""Representación de una adjudicación de acceso a un máster."""

from dataclasses import dataclass

from .corte import Corte
from .errores import ErrorDominio
from .master import Master


@dataclass(frozen=True)
class Adjudicacion:
    """Resultado de admisión de un máster en una convocatoria."""

    convocatoria: str
    master: Master
    corte: Corte

    def __post_init__(self) -> None:
        if not self.convocatoria.strip():
            raise ErrorDominio(
                "La convocatoria de una adjudicación no puede estar vacía."
            )
        if not isinstance(self.master, Master):
            raise ErrorDominio("La adjudicación necesita un máster válido.")
        if not isinstance(self.corte, Corte):
            raise ErrorDominio("La adjudicación necesita un corte válido.")