from collections.abc import Mapping
from dataclasses import dataclass
from decimal import Decimal

from .corte import CorteNumerico, EstadoCorte
from .errores import ErrorDominio
from .prioridad_carreras import PrioridadCarrera

@dataclass(frozen=True)
class Requisito:
    descripcion: str
    obligatorio: bool

    def __post_init__(self) -> None:
        if not isinstance(self.descripcion, str) or not self.descripcion.strip():
            raise ErrorDominio("La descripción del requisito no puede estar vacía.")
        if not isinstance(self.obligatorio, bool):
            raise ErrorDominio("El carácter obligatorio debe ser verdadero o falso.")

@dataclass(frozen=True)
class Criterio:
    nombre: str
    ponderacion: Decimal
    calculable: bool

    def __post_init__(self) -> None:
        if not isinstance(self.nombre, str) or not self.nombre.strip():
            raise ErrorDominio("El nombre del criterio no puede estar vacío.")
        if not isinstance(self.ponderacion, Decimal):
            raise ErrorDominio("La ponderación debe ser Decimal.")
        if not Decimal("0") <= self.ponderacion <= Decimal("100"):
            raise ErrorDominio("La ponderación debe estar entre 0 y 100.")
        if not isinstance(self.calculable, bool):
            raise ErrorDominio("La calculabilidad debe ser booleana.")

@dataclass(frozen=True)
class Acceso:
    prioridad: PrioridadCarrera
    requisitos: tuple[Requisito, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.prioridad, PrioridadCarrera):
            raise ErrorDominio("El acceso necesita una prioridad de carrera válida.")
        if not isinstance(self.requisitos, tuple) or not all(
            isinstance(requisito, Requisito) for requisito in self.requisitos
        ):
            raise ErrorDominio("Los requisitos de acceso deben ser una tupla válida.")

@dataclass(frozen=True)
class Master:
    nombre: str
    accesos: Mapping[str, Acceso]
    criterios: tuple[Criterio, ...]
    requisitos: tuple[Requisito, ...]
    corte: CorteNumerico | EstadoCorte

    def __post_init__(self) -> None:
        if not isinstance(self.nombre, str) or not self.nombre.strip():
            raise ErrorDominio("El nombre del máster no puede estar vacío.")
        if not isinstance(self.accesos, Mapping):
            raise ErrorDominio("Los accesos deben estar indexados por nombre de titulación.")
        for titulacion, acceso in self.accesos.items():
            if not isinstance(titulacion, str) or not titulacion.strip():
                raise ErrorDominio("El nombre de la titulación no puede estar vacío.")
            if not isinstance(acceso, Acceso):
                raise ErrorDominio("Cada titulación debe asociarse a un acceso válido.")
        if not isinstance(self.criterios, tuple) or not all(
            isinstance(criterio, Criterio) for criterio in self.criterios
        ):
            raise ErrorDominio("Los criterios deben ser una tupla de criterios válidos.")
        if self.criterios and sum((c.ponderacion for c in self.criterios), Decimal("0")) != Decimal("100"):
            raise ErrorDominio("Las ponderaciones de los criterios deben sumar 100.")
        if not isinstance(self.requisitos, tuple) or not all(
            isinstance(requisito, Requisito) for requisito in self.requisitos
        ):
            raise ErrorDominio("Los requisitos generales deben ser una tupla válida.")
        if not isinstance(self.corte, (CorteNumerico, EstadoCorte)):
            raise ErrorDominio("El máster necesita un corte válido.")
