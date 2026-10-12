"""Representación del corte de admisión de un máster."""

from dataclasses import dataclass
from enum import Enum

from .errores import ErrorDominio
from .prioridad import Prioridad
from .puntuacion import Puntuacion


class EstadoCorte(Enum):
    """Situación del corte publicado para una adjudicación."""

    NUMERICO = "NUMERICO"
    TODOS_ADMITIDOS = "TODOS_ADMITIDOS"
    SIN_ADJUDICACION = "SIN_ADJUDICACION"


@dataclass(frozen=True)
class Corte:
    """Corte numérico o estado especial publicado por la fuente."""

    estado: EstadoCorte
    prioridad: Prioridad | None = None
    puntuacion: Puntuacion | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.estado, EstadoCorte):
            raise ErrorDominio("El estado del corte no es válido.")

        if self.estado is EstadoCorte.NUMERICO:
            if not isinstance(self.prioridad, Prioridad) or not isinstance(
                self.puntuacion, Puntuacion
            ):
                raise ErrorDominio(
                    "Un corte numérico necesita prioridad y puntuación."
                )
        elif self.estado is EstadoCorte.TODOS_ADMITIDOS:
            if self.prioridad is not Prioridad.RESTO or self.puntuacion is not None:
                raise ErrorDominio(
                    "El corte ** 0,01 debe conservar la prioridad RESTO y no "
                    "llevar una puntuación ordinaria."
                )
        elif self.prioridad is not None or self.puntuacion is not None:
            raise ErrorDominio(
                "Un corte sin adjudicación no puede incluir prioridad ni puntuación."
            )

    @classmethod
    def numerico(cls, prioridad: Prioridad, puntuacion: Puntuacion) -> "Corte":
        """Crea un corte con prioridad y puntuación conocidas."""
        return cls(EstadoCorte.NUMERICO, prioridad, puntuacion)

    @classmethod
    def todos_admitidos(cls) -> "Corte":
        """Representa ** 0,01, asociado a RESTO."""
        return cls(EstadoCorte.TODOS_ADMITIDOS, Prioridad.RESTO)

    @classmethod
    def sin_adjudicacion(cls) -> "Corte":
        """Representa el texto publicado como AÚN SIN ADJ."""
        return cls(EstadoCorte.SIN_ADJUDICACION)