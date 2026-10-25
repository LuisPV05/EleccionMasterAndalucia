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
    requisitos: tuple[Requisito, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.prioridad, PrioridadCarrera):
            raise ValueError("El acceso necesita una prioridad de carrera válida.")
        if not isinstance(self.requisitos, tuple) or not all(
            isinstance(requisito, Requisito) for requisito in self.requisitos
        ):
            raise ValueError("Los requisitos de acceso deben ser una tupla válida.")


class Master:
    def __init__(
        self,
        accesos: Mapping[str, Acceso],
        criterios: Mapping[str, Criterio],
        requisitos: tuple[Requisito, ...],
        corte: CorteNumerico | EstadoCorte,
    ) -> None:
        if not isinstance(accesos, Mapping):
            raise ValueError("Los accesos deben estar indexados por nombre de titulación.")
        for titulacion, acceso in accesos.items():
            if not isinstance(titulacion, str) or not titulacion.strip():
                raise ValueError("El nombre de la titulación no puede estar vacío.")
            if not isinstance(acceso, Acceso):
                raise ValueError("Cada titulación debe asociarse a un acceso válido.")
        if not isinstance(criterios, Mapping):
            raise ValueError("Los criterios deben estar indexados por nombre de criterio.")
        for nombre, criterio in criterios.items():
            if not isinstance(nombre, str) or not nombre.strip():
                raise ValueError("El nombre del criterio no puede estar vacío.")
            if not isinstance(criterio, Criterio):
                raise ValueError("Cada nombre de criterio debe asociarse a un criterio válido.")
        if criterios and sum((c.ponderacion for c in criterios.values()), Decimal("0")) != Decimal("100"):
            raise ValueError("Las ponderaciones de los criterios deben sumar 100.")
        if not isinstance(requisitos, tuple) or not all(
            isinstance(requisito, Requisito) for requisito in requisitos
        ):
            raise ValueError("Los requisitos generales deben ser una tupla válida.")
        self._accesos = accesos
        self._criterios = criterios
        self._requisitos = requisitos
        self.corte = corte

    @property
    def accesos(self) -> Mapping[str, Acceso]:
        return self._accesos

    @property
    def criterios(self) -> Mapping[str, Criterio]:
        return self._criterios

    @property
    def requisitos(self) -> tuple[Requisito, ...]:
        return self._requisitos

    @property
    def corte(self) -> CorteNumerico | EstadoCorte:
        return self._corte

    @corte.setter
    def corte(self, corte: CorteNumerico | EstadoCorte) -> None:
        if not isinstance(corte, (CorteNumerico, EstadoCorte)):
            raise ValueError("El máster necesita un corte válido.")
        self._corte = corte
