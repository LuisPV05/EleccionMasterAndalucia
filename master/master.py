from collections.abc import Mapping
from dataclasses import dataclass
from decimal import Decimal

from .corte import CorteNumerico, EstadoCorte
from .prioridad_carreras import PrioridadCarrera

@dataclass(frozen=True)
class Requisito:
    descripcion: str
    obligatorio: bool

    def __post_init__(self) -> None:
        if not isinstance(self.descripcion, str) or not self.descripcion.strip():
            raise ValueError("La descripción del requisito no puede estar vacía.")
        if not isinstance(self.obligatorio, bool):
            raise ValueError("El carácter obligatorio debe ser verdadero o falso.")

@dataclass(frozen=True)
class Criterio:
    ponderacion: Decimal
    calculable: bool

    def __post_init__(self) -> None:
        if not isinstance(self.ponderacion, Decimal):
            raise ValueError("La ponderación debe ser Decimal.")
        if not Decimal("0") <= self.ponderacion <= Decimal("100"):
            raise ValueError("La ponderación debe estar entre 0 y 100.")
        if not isinstance(self.calculable, bool):
            raise ValueError("La calculabilidad debe ser booleana.")

@dataclass(frozen=True)
class Acceso:
    prioridad: PrioridadCarrera
    codigos_requisitos: frozenset[str]

    def __post_init__(self) -> None:
        if not isinstance(self.prioridad, PrioridadCarrera):
            raise ValueError("El acceso necesita una prioridad de carrera válida.")
        if not isinstance(self.codigos_requisitos, frozenset) or not all(
            isinstance(codigo, str) and codigo.strip() for codigo in self.codigos_requisitos
        ):
            raise ValueError("Los códigos de requisitos del acceso deben ser un frozenset de textos no vacíos.")

@dataclass(eq=False)
class Master:
    accesos: Mapping[str, Acceso]
    criterios: Mapping[str, Criterio]
    requisitos: Mapping[str, Requisito]
    corte: CorteNumerico | EstadoCorte

    def __post_init__(self) -> None:
        if not isinstance(self.accesos, Mapping):
            raise ValueError("Los accesos deben estar indexados por nombre de titulación.")
        for titulacion, acceso in self.accesos.items():
            if not isinstance(titulacion, str) or not titulacion.strip():
                raise ValueError("El nombre de la titulación no puede estar vacío.")
            if not isinstance(acceso, Acceso):
                raise ValueError("Cada titulación debe asociarse a un acceso válido.")
        if not isinstance(self.criterios, Mapping):
            raise ValueError("Los criterios deben estar indexados por nombre de criterio.")
        for nombre, criterio in self.criterios.items():
            if not isinstance(nombre, str) or not nombre.strip():
                raise ValueError("El nombre del criterio no puede estar vacío.")
            if not isinstance(criterio, Criterio):
                raise ValueError("Cada nombre de criterio debe asociarse a un criterio válido.")
        if self.criterios and sum((c.ponderacion for c in self.criterios.values()), Decimal("0")) != Decimal("100"):
            raise ValueError("Las ponderaciones de los criterios deben sumar 100.")
        if not isinstance(self.requisitos, Mapping):
            raise ValueError("Los requisitos deben estar indexados por código de requisito.")
        for codigo, requisito in self.requisitos.items():
            if not isinstance(codigo, str) or not codigo.strip():
                raise ValueError("El código del requisito no puede estar vacío.")
            if not isinstance(requisito, Requisito):
                raise ValueError("Cada código de requisito debe asociarse a un requisito válido.")
        for acceso in self.accesos.values():
            if not acceso.codigos_requisitos <= self.requisitos.keys():
                raise ValueError("Los códigos de requisitos de cada acceso deben existir en el máster.")
        if not isinstance(self.corte, (CorteNumerico, EstadoCorte)):
            raise ValueError("El máster necesita un corte válido.")
