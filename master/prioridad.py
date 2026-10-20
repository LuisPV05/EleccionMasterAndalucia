from enum import Enum

class Prioridad(Enum):
    ALTA = "ALTA"
    MEDIA = "MEDIA"
    BAJA = "BAJA"
    RESTO = "RESTO"

    @property
    def orden(self) -> int:
        return {
            Prioridad.ALTA: 1,
            Prioridad.MEDIA: 2,
            Prioridad.BAJA: 3,
            Prioridad.RESTO: 4,
        }[self]
