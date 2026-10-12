
"""Objeto de valor que representa la prioridad de una titulación.""" 

from enum import Enum


class Prioridad(Enum):
    """Prioridad de una titulación para acceder a un máster."""

    ALTA = "ALTA"
    MEDIA = "MEDIA"
    BAJA = "BAJA"
    RESTO = "RESTO"
