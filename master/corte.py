
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
    """Representa el corte y conserva su significado dentro del dominio."""

    estado: EstadoCorte
    prioridad: Prioridad | None = None
    puntuacion: Puntuacion | None = None

    def __post_init__(self) -> None:
        if self.estado == EstadoCorte.NUMERICO:
            if self.prioridad is None or self.puntuacion is None:
                raise ErrorDominio(
                    "Un corte numérico necesita prioridad y puntuación."
                )
        elif self.prioridad is not None or self.puntuacion is not None:
            raise ErrorDominio(
                "Un corte especial no puede tener prioridad ni puntuación "
                "numérica asociadas en este modelo."
            )

    @classmethod
    def numerico(
        cls,
        prioridad: Prioridad,
        puntuacion: Puntuacion,
    ) -> "Corte":
        """Crea un corte con prioridad y puntuación conocidas."""
        return cls(
            estado=EstadoCorte.NUMERICO,
            prioridad=prioridad,
            puntuacion=puntuacion,
        )

    @classmethod
    def todos_admitidos(cls) -> "Corte":
        """Representa el valor especial publicado como ** 0,01."""
        return cls(estado=EstadoCorte.TODOS_ADMITIDOS)

    @classmethod
    def sin_adjudicacion(cls) -> "Corte":
        """Representa el estado publicado como AÚN SIN ADJ."""
        return cls(estado=EstadoCorte.SIN_ADJUDICACION)
